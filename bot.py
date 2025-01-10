from discord.ext.commands import Cog
import asyncio
from pathlib import Path
import logging
from typing import Dict, Any
import json
import importlib.util

class File:
    def __init__(self, bot: object, config_path: Path = Path('config.json')):
        self.bot = bot
        self.config_path = config_path
        self._cogs: list[Cog] = []

        try:
            with open(self.config_path, 'r') as config_file:
                self.load_config_from_json(config_file)
        except (FileNotFoundError, json.JSONDecodeError):
            logging.warning(f"Skipping invalid JSON in {self.config_path}")

    async def load_cogs(self) -> None:
        await self.load_config()
        
        cog_data = self._config.get('filename_pattern', [])

        if not self._config or not cog_data:
            cogs_to_import = [file for file in self.path.glob('*') if file.is_file() and file.suffix == '.py']
            self._cogs.extend(self.import_cog(file) for file in cogs_to_import)
        
        self.bot.add_cogs(self._cogs)

    def load_config_from_json(self, config_file: Path) -> None:
        with config_file.open('r') as json_file:
            self._config = json.load(json_file)
        self._cogs.clear()

    def import_cog(self, file: Path) -> Cog:
        spec = importlib.util.spec_from_file_location(
            'cogs',
            str(file)
        )
        cog_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cog_module)
        return type('Cog', (Cog,), cog_module.__dict__)

    def load_config(self) -> None:
        if not self._config or len([file for file in self.path.glob('*') if file.is_file() and file.suffix == '.py']) != 1:
            try:
                with open(str(self.config_path), 'r') as config_file:
                    self.load_config_from_json(config_file)
            except (FileNotFoundError, json.JSONDecodeError):
                logging.warning(f"Skipping invalid JSON in {self.config_path}")
        if not self._config or len([file for file in self.path.glob('*') if file.is_file() and file.suffix == '.py']) != 1:
            return
    
    @property
    def config(self) -> Dict[str, Any]:
        return self._config.copy()
    
    @config.setter
    def config(self, value: Dict[str, Any]) -> None:
        self._config = value