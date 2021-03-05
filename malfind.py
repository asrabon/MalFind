from configparser import ConfigParser
import logging
import os
import string

import click

# Local Python Imports
import malware_bazaar
import hybrid_analysis


API_KEY_REQUIRED = [
    "Hybrid-Analysis"
]

SEARCH_FUNCTIONS = [
    ("Hybrid-Analysis", hybrid_analysis.search),
    ("Malware Bazaar", malware_bazaar.search),
]

CONFIG_FILE = os.path.join("./", "config.ini")


@click.command()
@click.option('--hash', required=True, help='Hash to search for online.')
def search(hash):
    if len(hash) not in [32, 40, 64] or any(char not in string.hexdigits for char in hash):
        click.echo("File hash entered is invalid. Please enter an MD5, SHA1, or SHA256 hash.")
    
    # Load config file if available
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
    
    for source, source_func in SEARCH_FUNCTIONS:
        if source in API_KEY_REQUIRED:
            if config:
                api_key = config[source]["api-key"]
            else:
                logging.warning(f"Unable to search {source} no config file loaded...")
                continue

        click.echo(f"Searching {source} for {hash}...")
        try:
            if source in API_KEY_REQUIRED:
                urls = source_func(hash, api_key)
            else:
                urls = source_func(hash)

            if urls:
                click.echo(f"{hash} found on {source}")
                click.echo(urls)
            else:
                click.echo(f"{hash} not found on {source}")
            click.echo()
        except Exception as e:
            logging.error(f"Exception occurred while searching {source}: {e}")


if __name__ == '__main__':
    search()
