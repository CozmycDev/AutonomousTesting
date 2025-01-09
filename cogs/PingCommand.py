from discord import Option
from discord.commands import slash_command
from discord.ext import commands


class PingCommand(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @slash_command(name='ping', description='Example slash command.')
    async def test_command(self, ctx: discord.ApplicationContext, test_string: Option(str, 'The string to say')):
        await ctx.defer()
        return f"User said {test_string}"

        
def setup(bot: commands.Bot) -> None:
    bot.add_cog(PingCommand(bot))