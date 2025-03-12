import os

# Base directory of the project (root directory)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Config paths
CONFIG_DIR = os.path.join(BASE_DIR, "config")
CONFIG_TEMPLATE = os.path.join(CONFIG_DIR, "config_template.ini")
CONFIG_PROD = os.path.join(CONFIG_DIR, "config.ini")

# Data directories
DATA_DIR = os.path.join(BASE_DIR, "data")
CAPTURED_DIR = os.path.join(DATA_DIR, "captured_files")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed_files")
LOGS_DIR = os.path.join(DATA_DIR, "logs")
