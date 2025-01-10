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
        self.config_path = config_path
        self._config: Dict[str, Any] = {}

        # Load or create the configuration file if it doesn't exist
        try:
            with open(str(self.config_path), 'r') as config_file:
                self._config = json.load(config_file)
        except (FileNotFoundError, json.JSONDecodeError):
            logging.warning(f"Skipping invalid JSON in {self.config_path}")
        
    async def load_cogs(self) -> None:
        # Refresh the configuration before loading cogs
        if not self._config or 'filename_pattern' not in self._config:
            try:
                with open(str(self.config_path), 'r') as config_file:
                    self._config = json.load(config_file)
            except (FileNotFoundError, json.JSONDecodeError):
                logging.warning(f"Skipping invalid JSON in {self.config_path}")
        
        # Load cogs only if the configuration exists
        cog_data = self._config.get('filename_pattern', [])
        if not self._config:
            return
        
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
        pass

    @property
    def config(self) -> Dict[str, Any]:
        return self._config.copy()

    @config.setter
    def config(self, value: Dict[str, Any]) -> None:
        self._config = value