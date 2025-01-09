import discord
from cogwatch import Watcher
from config_util import load, GLOBAL_CONFIG
from typing import Optional

class Bot:
    def __init__(self):
        self.intents = discord.Intents.default()
        self.bot = discord.Bot(intents=self.intents)

    @bot.event
    async def on_ready(self):
        self.watcher_config = self._get_watcher_config()
        self.watcher = Watcher(bot=self.bot, path='cogs', **self.watcher_config)
        await self.watcher.start()  
        await self.bot.sync_commands()

        print("--------------------------------------")
        print(f"Logged in as {self.bot.user} (v{GLOBAL_CONFIG.get('main.version')})")
        print("--------------------------------------")

    @staticmethod
    async def run(config_util: Optional[dict] = None) -> None:
        config_util = config_util or {}
        await config_util.load()
        bot = Bot()
        await bot.run(GLOBAL_CONFIG['DISCORD_TOKEN'])

    def _get_watcher_config(self) -> dict:
        return {
            'preload': True,
            'debug': False
        }

if __name__ == "__main__":
    import asyncio
    loop = asyncio.GetEventLoop()
    loop.create_task(Bot.run())