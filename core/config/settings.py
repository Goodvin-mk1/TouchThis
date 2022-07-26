from json import load

from schemas.config import ConfigSchema


def load_config() -> ConfigSchema:
    with open("config.json", "r", encoding="utf-8") as file:
        return ConfigSchema(**load(file))


CONFIG: ConfigSchema = load_config()
