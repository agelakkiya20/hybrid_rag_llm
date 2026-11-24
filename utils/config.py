
import yaml
from pathlib import Path

def load_config():
    config_path = Path("configs/base.yaml")

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config

if __name__ == "__main__":
    config = load_config()
    print(config)