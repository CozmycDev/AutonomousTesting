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

    class Commands(commands.Cog):
        pass

class PingError(Exception):
    """Custom exception for ping errors."""
    pass