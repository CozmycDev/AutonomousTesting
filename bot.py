from discord.ext.commands import Cog
import asyncio
from pathlib import Path
import logging
from typing import Dict, List
import json
import importlib.util

class File:
    def __init__(self, path: Path, filename_pattern: List[str] = ['cogs/*.py']):
        self.path = path
        self.filename_pattern = filename_pattern
        self.config: Dict[str, str] = {}

    async def load_cogs(self) -> None:
        await self.load_config()
        cog_data = self.config.get('filename_pattern', [])
        for file in self.path.glob('*'):
            if file.is_file() and file.suffix == '.py':
                if str(file).endswith(tuple(cog_data)):
                    self.bot.add_cog(Cog(await self.import_cog(file)))

    async def import_cog(self, file: Path) -> Cog:
        spec = importlib.util.spec_from_file_location(
            'cogs',
            file
        )
        cog_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cog_module)
        return type('Cog', (Cog,), cog_module.__dict__)

    async def load_config(self) -> Dict[str, str]:
        config_path = self.path / 'config.json'
        if config_path.exists():
            with open(str(config_path), 'r') as config_file:
                try:
                    return json.load(config_file)
                except json.JSONDecodeError:
                    logging.warning(f"Skipping invalid JSON in {config_path}")
                    return {}
        else:
            logging.error(f"No config file found at {self.path}")
            return {}

    def add_cog(self, cog: Cog) -> None:
        self.bot.add_cog(cog)

    def save_config(self, config: Dict[str, str]) -> None:
        config_path = self.path / 'config.json'
        with open(str(config_path), 'w') as config_file:
            json.dump(config, config_file)