import logging
import os
import string

import click

# Local Python Imports
import hybrid_analysis
import malshare
import malquarium
import malware_bazaar
import virus_share

from util import load_config


API_KEY_REQUIRED = [
    "Hybrid-Analysis",
    "MalShare"
]

LOGIN_REQUIRED = [
    "VirusShare"
]

SEARCH_FUNCTIONS = [
    ("Hybrid-Analysis", hybrid_analysis.search),
    ("Malware Bazaar", malware_bazaar.search),
    ("VirusShare", virus_share.search),
    ("Malquarium", malquarium.search),
    ("MalShare", malshare.search),
]


@click.command()
@click.option('--hash', required=True, help='Hash to search for online.')
def search(hash):
    if len(hash) not in [32, 40, 64] or any(char not in string.hexdigits for char in hash):
        click.echo("File hash entered is invalid. Please enter an MD5, SHA1, or SHA256 hash.")
    
    # Load config file if available
    config = load_config()
    
    for source, source_func in SEARCH_FUNCTIONS:
        if source in API_KEY_REQUIRED:
            if config:
                api_key = config[source]["api-key"]
            else:
                logging.warning(f"Unable to search {source} no config file loaded...")
                continue
        elif source in LOGIN_REQUIRED:
            if config:
                username, password = config[source]["username"], config[source]["password"]
            else:
                logging.warning(f"Unable to search {source} no config file loaded...")
                continue

        click.echo(f"Searching {source} for {hash}...")
        try:
            if source in API_KEY_REQUIRED:
                urls = source_func(hash, api_key)
            elif source in LOGIN_REQUIRED:
                urls = source_func(hash, username, password)
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
