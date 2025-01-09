from typing import Optional
import asyncio
import traceback
import discord
from cogwatch import Watcher
from config_util import load, GLOBAL_CONFIG

class Bot:
    def __init__(self):
        self._intents = discord.Intents.default()
        self.bot = discord.Bot(intents=self._intents)

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
        await bot.watcher.start()

    async def __aenter__(self) -> None:
        try:
            self.watcher_config = await self._get_watcher_config()
            self.watcher = Watcher(bot=self.bot, path='cogs', **self.watcher_config)
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
        # Implement logic to fetch watcher config from a reliable source
        # For demonstration purposes, return a hardcoded configuration
        return {
            'path': 'cogs',
            'filename_pattern': '*.py'
        }