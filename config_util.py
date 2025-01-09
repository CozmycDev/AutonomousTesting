def load_dotenv():
    import os
    import json
    import io
    import traceback

    os.environ.clear()
    with open(".env", "r") as env_file:
        for line in env_file.readlines():
            key, value = line.strip().split("=")
            os.environ[key] = value


def load_environment_variables():
    from dotenv import load_dotenv
    load_dotenv()

    return dict(os.environ)


ENVIRONMENT_VARIABLES = load_environment_variables()
GLOBAL_CONFIG = {}

class FileSection:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, config, key):
        section = None
        parts = key.split('.')
        for part in parts:
            if section is None:
                section = cls(name=part)
            else:
                section = getattr(section, f"_{part}")
        
        return section

    @property
    def save_to_json(self, config):
        return f'"{self.name}":{{{{"json": self.value.save_to_json()}}}}'

    def save_to_file(self, file_name):
        import json
        with open(file_name, "w") as file:
            json.dump({self.name: {key: value for key, value in self.items()}}, file)

    @property
    def items(self):
        return {key: value for section in [self] for key, value in getattr(section, f"_{name}", {}).items() if name}