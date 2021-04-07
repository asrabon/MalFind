# Standard Python Libraries
from configparser import ConfigParser
import os

# 3rd Party Python Libraries
from termcolor import colored

CONFIG_FILE = os.path.join("./", "config.ini")

def load_config():
    config = None
    if os.path.exists(CONFIG_FILE):
        try:
            config = ConfigParser()
            config.read(CONFIG_FILE)
        except Exception as e:
            config = None
            print(colored(f"Unable to load config file: {e}", "red"))
    else:
        print(colored(f"Config file does not exist please modify config.ini.example with your information to get the full benefits of the application", "red"))
    
    return config