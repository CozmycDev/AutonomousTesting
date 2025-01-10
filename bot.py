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
        for file in self.path.glob('cogs/*.py'):
            if file.is_file():
                cog_data = await self.import_cog(file)
                self.bot.add_cog(Cog(cog_data))

    async def import_cog(self, file: Path) -> Cog:
        with open(str(file), 'r') as file_obj:
            cog_data = file_obj.read()
        return Cog.from_type(Cog, cog_data)

    def stop(self):
        self.bot.remove_listener('on_ready', self.on_ready)

class Bot:
    # ... (rest of the class remains the same)