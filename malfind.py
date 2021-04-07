import os
import string

# 3rd Party Python Libraries
import click
from colorama import init
from termcolor import colored

# Local Python Imports
from sources import *

from util import load_config


# Setup Colorama
init()


# Constants
API_KEY_REQUIRED = [
    "Hybrid-Analysis",
    "MalShare"
]

LOGIN_REQUIRED = [
    "VirusShare"
]

SEARCH_FUNCTIONS = [
    ("Hybrid-Analysis", hybrid_analysis.search),
    ("MalShare", malshare.search),
    ("Malware Bazaar", malware_bazaar.search),
    ("VirusShare", virus_share.search),
    ("Malquarium", malquarium.search),
    ("MalShare", malshare.search),
    ("PolySwarm", polyswarm.search),
    ("Triage", triage.search),
    ("UrlHaus", url_haus.search),
    ("VirusBay", virus_bay.search)
]


@click.command()
@click.option('--hash', required=True, help='Hash to search for online.')
def search(hash):
    if len(hash) not in [32, 40, 64] or any(char not in string.hexdigits for char in hash):
        print(colored("File hash entered is invalid. Please enter an MD5, SHA1, or SHA256 hash.", "red"))
    
    # Load config file if available
    config = load_config()
    
    for source, source_func in SEARCH_FUNCTIONS:
        if source in API_KEY_REQUIRED:
            if config:
                api_key = config[source]["api-key"]
            else:
                print(colored(f"Unable to search {source} no config file loaded...\n", "red"))
                continue
        elif source in LOGIN_REQUIRED:
            if config:
                username, password = config[source]["username"], config[source]["password"]
            else:
                print(colored(f"Unable to search {source} no config file loaded...\n", "red"))
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
                print(colored(f"{hash} found on {source}", "green"))

                if isinstance(urls, list):
                    for url in urls:
                        print(colored(url, "blue"))
                else:
                    print(colored(urls, "blue"))
            else:
                print(f"{hash} not found on {source}")

        except Exception as e:
            print(colored(f"Exception occurred while searching {source}: {e}", "red"))
        finally:
            print()


if __name__ == '__main__':
    search()
