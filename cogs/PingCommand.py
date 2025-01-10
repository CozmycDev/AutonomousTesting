from discord import app_commands
from discord.ext import commands
import logging
from typing import Optional

class PingCommand(commands.Cog):
    """Ping command cog."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @app_command(name='ping', description="The input string to say", options=[Option("string", "Input string.", True)])
    async def ping(self, ctx: app_commands.Context, test_string: Optional[str] = None):
        """Test command that returns the input string."""
        self.logger.info(f"Command {ctx.command.name} invoked")
        await ctx.defer()
        return f"Pong! User said {test_string or 'Default message'}"

class PingError(Exception):
    """Custom exception for ping errors."""
    pass