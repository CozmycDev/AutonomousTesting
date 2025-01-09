from discord import Option
from discord.commands import slash_command
from discord.ext import commands


class PingCommand(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @slash_command(name='ping', description='Example slash command.')
    @Option(
        "test_string",
        str,
        description="User input string",
        required=True
    )
    async def test_command(self, ctx: discord.ApplicationContext, test_string: str):
        await ctx.defer()
        await ctx.respond(content=f"User said {test_string}")
        
        
def setup(bot: commands.Bot) -> None:
    bot.add_cog(PingCommand(bot))