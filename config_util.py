import os
import json
import io
import traceback

load_dotenv()


def load_environment_variables():
    env_vars = {key: value for key, value in os.environ.items()}
    return env_vars


ENVIRONMENT_VARIABLES = load_environment_variables()
GLOBAL_CONFIG = {}


def load():
    global GLOBAL_CONFIG

    try:
        with open("bot_config.json", "r") as config_file:
            config = json.load(config_file)

        for section, values in config.items():
            for key, value in values.items():
                GLOBAL_CONFIG[f"{section}.{key}"] = value

        for key, value in ENVIRONMENT_VARIABLES.items():
            if value:
                GLOBAL_CONFIG[key] = value

    except FileNotFoundError:
        print("Configuration file not found. Please ensure 'bot_config.json' exists.")
    except json.JSONDecodeError:
        print("Error decoding JSON from the configuration file.")
    except Exception as e:
        print(f"An unexpected error occurred while loading the configuration: {e}")
        traceback.print_exc()


def save():
    global GLOBAL_CONFIG

    try:
        config = {}

        for key, value in GLOBAL_CONFIG.items():
            section, sub_key = key.split('.', 1)
            if section not in config:
                config[section] = {}
            config[section][sub_key] = value

        json_config = json.dumps(config, indent=4)
        with io.open("bot_config.json", 'w', encoding='utf-8') as config_file:
            config_file.write(json_config)

    except IOError:
        print("An error occurred while writing to the configuration file.")
    except Exception as e:
        print(f"An unexpected error occurred while saving the configuration: {e}")
        traceback.print_exc()
