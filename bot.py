import discord
from cogwatch import Watcher
from config_util import load, GLOBAL_CONFIG

class Bot:
    def __init__(self):
        self.intents = discord.Intents.default()
        self.bot = discord.Bot(intents=self.intents)

    @bot.event
    async def on_ready(self):
        watcher = Watcher(bot=self.bot, path='cogs', preload=True, debug=False)
        await watcher.start()  
        await self.bot.sync_commands()

        print("--------------------------------------")
        print(f"Logged in as {self.bot.user} (v{GLOBAL_CONFIG.get('main.version')})")
        print("--------------------------------------")

    @staticmethod
    async def run(config_util):
        config_util.load()
        bot = Bot()
        await bot.run(GLOBAL_CONFIG['DISCORD_TOKEN'])

if __name__ == "__main__":
    import asyncio
    loop = asyncio.GetEventLoop()
    loop.create_task(Bot.run(load))

#