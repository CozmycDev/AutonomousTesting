import discord
import asyncio
from pathlib import Path
from discord.ext.commands import app_commands

class Bot:
    def __init__(self):
        self._intents = discord.Intents.default()
        self.bot = discord.Bot(intents=self._intents)
        self.watcher_config = None
        self.watcher = None

    @property
    async def watcher_config(self) -> dict:
        return await self._get_watcher_config()

    @staticmethod
    async def run(config_util: Optional[dict] = None) -> None:
        config_util = config_util or {}
        await config_util.load()
        bot = Bot()
        await bot.run(GLOBAL_CONFIG['DISCORD_TOKEN'])

    @staticmethod
    async def start_watcher() -> None:
        bot = Bot()
        await bot.watcher_config

    async def __aenter__(self) -> None:
        try:
            self.watcher_config = await self._get_watcher_config()
            self.watcher = Watcher(bot=self.bot, path=Path('cogs'), **self.watcher_config)
            await self.watcher.start()
            await self.bot.sync_commands()
        except Exception as e:
            traceback.print_exc()

    async def __aexit__(self, exc_type: Optional[type], exc_value: Optional[Exception], traceback: Optional[traceback.TracebackType]) -> None:
        try:
            if not issubclass(exc_type, KeyboardInterrupt):
                raise exc_value
            self.watcher.stop()
            await self.bot.close()
        except Exception as e:
            traceback.print_exc()

    @classmethod
    def bot(cls) -> 'Bot':
        return cls()

    async def _get_watcher_config(self) -> dict:
        config_file = Path('watcher_config.json')
        if not config_file.exists():
            raise FileNotFoundError(f'Watcher configuration file {config_file} not found.')
        with open(config_file, 'r') as config_file:
            config_data = json.load(config_file)
        watcher_config = config_data.get('config', {})
        watcher_config['path'] = Path('cogs')
        watcher_config['filename_pattern'] = '*.py'
        return watcher_config

    async def _load_watcher_config(self) -> None:
        await self._get_watcher_config()
        self.watcher.stop()

    async def _update_watcher_config(self, new_config: dict) -> None:
        if not new_config:
            raise ValueError('Watcher configuration cannot be empty.')
        self.watcher_config = new_config
        self.watcher = Watcher(bot=self.bot, path=Path('cogs'), **self.watcher_config)
        await self.watcher.start()

    async def _sync_commands(self) -> None:
        if not hasattr(self, 'bot') or not self.bot.is_ready():
            raise Exception('Commands can only be synced when the bot is ready.')
        commands = [cmd for cmd in app_commands.all_commands(self.bot) if cmd.cog_name == 'cogs']
        await commands[0].invoke()

    async def sync_commands_with_cogs(self) -> None:
        if not self.watcher_config['path'].is_dir():
            raise FileNotFoundError(f'Cogs path {self.watcher_config["path"]} does not exist.')
        for filename in self.watcher_config['filename_pattern'].glob('cogs/*.py'):
            if filename.is_file():
                cogs = await import_cog(filename)
                await self.bot.add_cog(cogs)

async def import_cog(filename: str) -> app_commands.Cog:
    with open(filename, 'r') as file:
        cog_data = file.read()
    return app_commands.Cog.from_type(app_commands.Cog, cog_data)