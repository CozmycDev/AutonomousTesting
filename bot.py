from discord.ext.commands import Cog
import asyncio
from pathlib import Path
import logging
from typing import Dict, Any
import json
import importlib.util

class File:
    def __init__(self, bot: object, config_path: Path):
        self.bot = bot
        self.config_path = config_path
        self._cogs = []
        self.config_data: Dict[str, Any] = None  # Use type annotation for better readability

        self.load_config()

    async def load_cogs(self) -> None:
        await self.load_config()
        filename_pattern = self.filename_pattern
        
        # Ensure cogs are reloaded when config is updated
        self._cogs.clear()
        
        for file in self.path.glob('*'):
            if file.is_file() and file.suffix == '.py':
                cog_module = self.import_cog(file)
                self._cogs.append(cog_module)

        self.bot.add_cogs(self._cogs)

    @property
    def config(self) -> Dict[str, Any]:
        return self.config_data

    async def load_config(self) -> None:
        if not self.config_data:
            try:
                with open(str(self.config_path), 'r') as config_file:
                    await self.load_config_from_json(config_file)
            except (FileNotFoundError, json.JSONDecodeError):
                logging.warning(f"Skipping invalid JSON in {self.config_path}")
        
        # TODO: Create separate method to load filename pattern configuration

    def import_cog(self, file: Path) -> Cog:
        spec = importlib.util.spec_from_file_location(
            'cogs',
            str(file)
        )
        cog_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cog_module)
        return type('Cog', (Cog,), cog_module.__dict__)

    def load_config_from_json(self, config_file: Path) -> None:
        try:
            self.config_data = json.load(config_file)
        except json.JSONDecodeError as e:
            logging.warning(f"Skipping invalid JSON in {self.config_path}: {e}")
        else:
            # Clear cogs before reloading them to ensure accurate file tracking
            self._cogs.clear()

    def load_filename_pattern(self, filename_pattern: list[str]) -> None:
        self.filename_pattern = filename_pattern
        self.load_cogs()