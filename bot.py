from discord.ext.commands import Cog
import asyncio
from pathlib import Path
import logging
from typing import Dict, List

class Watcher:
    def __init__(self, bot, path: Path, **config: Dict[str, str]):
        self.bot = bot
        self.path = path
        self.config = config

    async def start(self):
        filename_pattern: List[str] = self.config.get('filename_pattern', [])
        for file in self.path.glob('cogs/*.py'):
            if file.is_file():
                cog_data: str = await self.import_cog(file)
                self.bot.add_cog(Cog(cog_data))

    async def import_cog(self, file: Path) -> Cog:
        with open(str(file), 'r') as file_obj:
            cog_data: str = file_obj.read()
        return Cog.from_type(Cog, cog_data)

    def stop(self):
        self.bot.remove_listener('on_ready', self.on_ready)


class Bot:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.watcher = Watcher(self, Path(__file__).parent, filename_pattern=['cogs/*.py'])

    async def run(self):
        await self.watcher.start()
        # ... (rest of the class remains the same)