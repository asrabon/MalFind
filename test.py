# Local Python Imports
import hybrid_analysis
import malshare
import malquarium
import malware_bazaar
import virus_share

from util import load_config


def test_hybrid_anlysis():
    config = load_config()

    if config:
        api_key = config["Hybrid-Analysis"]["api-key"]
        urls = hybrid_analysis.search("2548e6fc9eb17e55d22dcfb4bf27212d", api_key)

        if urls is None:
            raise Exception("Unable to properly search Hybrid-Analysis")
    else:
        raise Exception("No config file available to test Hybrid-Analysis")


def test_malshare():
    config = load_config()

    if config:
        api_key = config["MalShare"]["api-key"]
        urls = malshare.search("bf0789bd659fba03fc870d531b740facbc583d45", api_key)

        if urls is None:
            raise Exception("Unable to properly search MalShare")
    else:
        raise Exception("No config file available to test MalShare")


def test_malquarium():
    urls = malquarium.search("f54093f3b5e316c9092c4bbd107f7ec304b217ca")

    if urls is None:
        raise Exception("Unable to properly search Malfind")


def test_malware_bazaar():
    urls = malware_bazaar.search("f54093f3b5e316c9092c4bbd107f7ec304b217ca")

    if urls is None:
        raise Exception("Unable to properly search Malware Bazaar")


def test_virus_share():
    config = load_config()

    if config:
        username, password = config["VirusShare"]["username"], config["VirusShare"]["password"]
        urls = virus_share.search("4c9f110b92d9ba479eb006bb9c81a9c0f1bf44ca", username, password)

        if urls is None:
            raise Exception("Unable to properly search VirusShare")
    else:
        raise Exception("No config file available to test VirusShare")
