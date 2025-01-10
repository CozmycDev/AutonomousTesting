from discord.ext.commands import Cog
import asyncio
from pathlib import Path
import logging
from typing import Dict, List

class File:
    def __init__(self, path: Path, config: Dict[str, str]):
        self.path = path
        self.config = config

    async def load_cogs(self) -> None:
        for file in self.path.glob('cogs/*.py'):
            if file.is_file():
                cog_data = await self.import_cog(file)
                self.bot.add_cog(Cog(cog_data))

    async def import_cog(self, file: Path) -> Cog:
        with open(str(file), 'r') as file_obj:
            try:
                cog_data = json.load(file_obj)
            except json.JSONDecodeError:
                logging.warning(f"Skipping invalid JSON in {file}")
                continue
        return Cog.from_type(Cog, cog_data)

    @staticmethod
    async def load_config(path: Path) -> Dict[str, str]:
        with open(str(path), 'r') as config_file:
            try:
                config = json.load(config_file)
            except json.JSONDecodeError:
                logging.warning(f"Skipping invalid JSON in {path}")
                return {}
        return config

class File:
    def __init__(self, path: Path, filename_pattern: List[str] = ['cogs/*.py']):
        self.path = path
        self.filename_pattern = filename_pattern

    async def start(self) -> None:
        await self.load_cogs()

    async def load_cogs(self) -> None:
        config = await File.load_config(self.path)
        cog_data = config.get('filename_pattern', [])
        for file in self.path.glob('*'):
            if str(file).endswith('.py') and file.is_file():
                if str(file) in cog_data:
                    self.bot.add_cog(Cog(await self.import_cog(file)))

    @staticmethod
    async def load_config(path: Path) -> Dict[str, str]:
        with open(str(path), 'r') as config_file:
            try:
                config = json.load(config_file)
            except json.JSONDecodeError:
                logging.warning(f"Skipping invalid JSON in {path}")
                return {}
        return config

    @staticmethod
    async def import_cog(file: Path) -> Cog:
        with open(str(file), 'r') as file_obj:
            try:
                cog_data = json.load(file_obj)
            except json.JSONDecodeError:
                logging.warning(f"Skipping invalid JSON in {file}")
                return Cog()
            else:
                return Cog.from_type(Cog, cog_data)