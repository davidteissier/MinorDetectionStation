import configparser
import os

def load_config(config_path='config/config.ini'):
    """Load station configuration from config.ini file"""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    
    config = configparser.ConfigParser()
    config.read(config_path)
    
    return config

def validate_config(config):
    """Validate required configuration parameters"""
    required_params = {
        'System': ['station_id', 'latitude', 'longitude', 'altitude'],
        'Capture': ['camera_model', 'exposure_time']
    }
    
    for section, params in required_params.items():
        if section not in config:
            raise ValueError(f"Missing section: {section}")
        for param in params:
            if param not in config[section]:
                raise ValueError(f"Missing parameter: {param} in section {section}")