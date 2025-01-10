from discord.ext.commands import Cog
import asyncio
from pathlib import Path
import logging
from typing import Dict, List
import json  # NEW FILE:/END_FILE

class File:
    def __init__(self, path: Path, **config: Dict[str, str]):
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
            cog_data: dict = json.load(file_obj)
        return Cog.from_type(Cog, cog_data)

    @staticmethod
    def load_config(path: Path):
        with open(path, 'r') as config_file:
            config = json.load(config_file)
        return config

class Bot:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.watcher = File(Path(__file__).parent, filename_pattern=['cogs/*.py'])

    async def run(self):
        await self.watcher.start()
        # ... (rest of the class remains the same)