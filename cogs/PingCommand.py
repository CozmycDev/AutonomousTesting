from discord import app_commands
from discord.ext import commands
import logging
from typing import Optional
logging.config.fileConfig('repo/cogs/logging_config.py') 

class PingCommand(commands.Cog):
    """Ping command cog."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @app_command(name='ping', description="The string to say", options=[Option("string", "The input string.", True)])
    async def ping(self, ctx: app_commands.Context, test_string: Optional[str] = None):
        """Test command that returns the input string."""
        self.logger.info(f"Command {ctx.command.name} invoked")
        await ctx.defer()
        return f"User said {test_string or ''}"

class PingError(Exception):
    """Custom exception for ping errors."""
    pass

#