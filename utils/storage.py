import json
from pathlib import Path

CONFIG_PATH = Path("user_config.json")

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f)

def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            return json.load(f)
    return {}
