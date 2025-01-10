from discord.ext.commands import Cog
import asyncio
from pathlib import Path
import logging
from typing import Dict, List
import json
import importlib.util

class File:
    def __init__(self, bot, config_path: Path = Path('config.json')):
        self.bot = bot
        self.path = Path(__name__).parent
        self.config_path = config_path
        if not self.config_path.exists():
            with open(str(self.config_path), 'w') as config_file:
                json.dump({}, config_file)
        self.load_config()

    async def load_cogs(self):
        await self.load_config()
        cog_data = self.config.get('filename_pattern', [])
        for file in self.path.glob('*'):
            if file.is_file() and file.suffix == '.py':
                if str(file).endswith(tuple(cog_data)):
                    self.bot.add_cog(Cog(await self.import_cog(file)))

    def import_cog(self, file: Path) -> Cog:
        spec = importlib.util.spec_from_file_location(
            'cogs',
            file
        )
        cog_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cog_module)
        return type('Cog', (Cog,), cog_module.__dict__)

    def load_config(self) -> None:
        config_path = self.config_path
        if config_path.exists():
            with open(str(config_path), 'r') as config_file:
                try:
                    self.config = json.load(config_file)
                except json.JSONDecodeError:
                    logging.warning(f"Skipping invalid JSON in {config_path}")
        else:
            logging.error(f"No config file found at {self.path}")
            self.config = {}