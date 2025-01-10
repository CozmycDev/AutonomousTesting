from discord import Option
from discord.commands import slash_command
from discord.ext import commands


class PingCommand(commands.Cog):
    """Ping command cog."""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @slash_command(name='ping', description=Option('The string to say', 'The string to display.'), options=[Option("string", "The input string.", True)])
    async def test_command(self, ctx: discord.ApplicationContext, test_string: str):
        """Test command that returns the input string."""
        await ctx.defer()
        return f"User said {test_string}"
        
def setup(bot: commands.Bot) -> None:
    bot.add_cog(PingCommand(bot))
    bot.tree.sync()  # Ensure the slash command is synced with the Discord API

class PingController(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command(name='ping', description=Option('The string to say', 'The string to display.'), options=[Option("string", "The input string.", True)])
    async def ping(self, ctx: discord.ApplicationContext):
        """Ping command that returns a greeting."""
        await ctx.defer()
        return f"User said {ctx.invoked_with[0]}"

def load_cogs(bot: commands.Bot) -> None:
    from repo.cogs import PingCommand
    bot.add_cog(PingCommand(bot))
    bot.tree.sync()  # Ensure the slash command is synced with the Discord API