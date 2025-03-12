import configparser
import shutil
import os
from src.paths import CONFIG_TEMPLATE, CONFIG_PROD


def create_or_load_config():
    """
    Load the config.ini file or generate it from config_template.ini if it does not exist.
    """
    if not os.path.exists(CONFIG_PROD):
        print("Configuration file not found. Generating from template...")
        if os.path.exists(CONFIG_TEMPLATE):
            shutil.copy(CONFIG_TEMPLATE, CONFIG_PROD)
            print(f"Created '{CONFIG_PROD}' from '{CONFIG_TEMPLATE}'.")
        else:
            raise FileNotFoundError(f"Template file '{CONFIG_TEMPLATE}' is missing.")

    # Load the configuration
    config = configparser.ConfigParser()
    config.read(CONFIG_PROD)
    return config
