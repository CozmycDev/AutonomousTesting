import discord
from cogwatch import Watcher
from config_util import load, GLOBAL_CONFIG

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    watcher = Watcher(bot, path='cogs', preload=True, debug=False)
    await watcher.start()  
    await bot.sync_commands()  

    print("--------------------------------------")
    print(f"Logged in as {bot.user} (v{GLOBAL_CONFIG.get('main.version')})")
    print("--------------------------------------")


config_util.load()
bot.run(GLOBAL_CONFIG['DISCORD_TOKEN'])  # Logs the bot into Discord