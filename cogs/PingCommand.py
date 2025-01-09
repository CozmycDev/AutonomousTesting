import discord

from discord import option
from discord.commands import slash_command
from discord.ext import commands


# TODO: add all the commands and functionality you would expect to see for a Discord moderation bot. kick, ban, mute
# TODO: add listeners for broadcasting member join/leaves in a specific guild/channel.


class PingCommand(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @slash_command(name='ping', description='Example slash command.')
    @option(
        "test_string",
        str,
        description="",
        required=True
    )
    async def test_command(
        self,
        ctx: discord.ApplicationContext,
        test_string: str
    ):
        await ctx.defer()
        await ctx.respond(content=f"you said {test_string}")
        
        
def setup(bot: commands.Bot) -> None:
    bot.add_cog(PingCommand(bot))
