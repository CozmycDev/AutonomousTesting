import discord
from discord import option
from discord.commands import slash_command
from discord.ext import commands


class PingCommand(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @slash_command(name='ping', description='Example slash command.')
    async def test_command(
        self,
        ctx: discord.ApplicationContext,
        test_string: str
    ):
        await ctx.defer()
        await ctx.respond(content=f"you said {test_string}")
        
        
def setup(bot: commands.Bot) -> None:
    bot.add_cog(PingCommand(bot))


class PingHelper(commands.Cog):
    @commands.command(name="help")
    async def ping_helper(self, ctx):
        await ctx.send("This is a help command.")

import os
from discord import Intents

intents = discord.Intents.default()
intents.typing = False  # Disable global typing events to reduce overhead
intents.presences = False  # Disable global presence updates to reduce overhead


class CustomBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, intents=intents)


def main():
    bot = CustomBot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user} (v{discord.__version__})")
        
    @bot.command(name="ping")
    async def ping(ctx):
        await ctx.send("Pong!")
        
        
def run():
    bot.run(os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    main()