# Standard Python Libraries
from configparser import ConfigParser
import logging
import os

CONFIG_FILE = os.path.join("./", "config.ini")

def load_config():
    config = None
    if os.path.exists(CONFIG_FILE):
        try:
            config = ConfigParser()
            config.read(CONFIG_FILE)
        except Exception as e:
            config = None
            logging.error(f"Unable to load config file: {e}")
    else:
        logging.warning(f"Config file does not exist please modify config.ini.example with your information to get the full benefits of the application")
    
    return config