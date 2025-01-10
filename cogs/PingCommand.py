from discord import app_commands
from discord.ext import commands


class PingCommand(commands.Cog):
    """Ping command cog."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_command(name='ping', description="The string to say", options=[Option("string", "The input string.", True)])
    async def ping(self, ctx: app_commands.Context, test_string: str = None):
        """Test command that returns the input string."""
        await ctx.defer()
        return f"User said {test_string or ''}"

def setup(bot: commands.Bot) -> None:
    bot.add_cog(PingCommand(bot))
    bot.tree.sync()  # Ensure the slash command is synced with the Discord API

class PingController(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_command(name='ping', description="The string to say", options=[Option("string", "The input string.", True)])
    async def ping(self, ctx: app_commands.Context):
        """Ping command that returns a greeting."""
        await ctx.defer()
        return f"User said {ctx.invoked_with[0]}"



def load_cogs():
    # Existing function for loading cogs
    pass