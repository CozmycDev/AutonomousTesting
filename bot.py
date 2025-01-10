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
        self._cogs: list[Cog] = []

        try:
            with open(self.config_path, 'r') as config_file:
                self._load_config_from_json(config_file)
        except (FileNotFoundError, json.JSONDecodeError):
            logging.warning(f"Skipping invalid JSON in {self.config_path}")

    async def load_cogs(self) -> None:
        await self.load_config()
        
        filename_pattern = self._config.get('filename_pattern', [])
        self._cogs.clear()

        for file in self.path.glob('*'):
            if file.is_file() and file.suffix == '.py':
                cog_module = self.import_cog(file)
                self._cogs.append(cog_module)

        self.bot.add_cogs(self._cogs)

    @property
    def config(self) -> Dict[str, Any]:
        return self._config

    async def load_config(self) -> None:
        if not self._config:
            try:
                with open(str(self.config_path), 'r') as config_file:
                    await self._load_config_from_json(config_file)
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

    def _load_config_from_json(self, config_file: Path) -> None:
        self._config = json.load(config_file)
        self._cogs.clear()