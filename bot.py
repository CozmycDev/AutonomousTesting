from discord.ext.commands import Cog
import asyncio
from pathlib import Path

class Watcher:
    def __init__(self, bot, path, **config):
        self.bot = bot
        self.path = Path(path)
        self.config = config

    async def start(self):
        filename_pattern = self.config.get('filename_pattern', [])
        for filename in filename_pattern.glob(self.path / 'cogs/*.py'):
            if filename.is_file():
                cog_data = await self.import_cog(filename)
                self.bot.add_cog(Cog(cog_data))

    async def import_cog(self, filename: str) -> Cog:
        with open(filename, 'r') as file:
            cog_data = file.read()
        return Cog.from_type(Cog, cog_data)

    def stop(self):
        self.bot.remove_listener('on_ready', self.on_ready)

class Bot:
     # ... (rest of the class remains the same)