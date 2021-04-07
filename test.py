# Local Python Imports
from sources import *
from util import load_config


def test_hybrid_anlysis():
    config = load_config()

    if config:
        api_key = config["Hybrid-Analysis"]["api-key"]
        urls = hybrid_analysis.search("2548e6fc9eb17e55d22dcfb4bf27212d", api_key)

        assert urls is not None
    else:
        raise Exception("No config file available to test Hybrid-Analysis")


def test_malshare():
    config = load_config()

    if config:
        api_key = config["MalShare"]["api-key"]
        urls = malshare.search("bf0789bd659fba03fc870d531b740facbc583d45", api_key)

        assert urls is not None
    else:
        raise Exception("No config file available to test MalShare")


def test_malquarium():
    urls = malquarium.search("f54093f3b5e316c9092c4bbd107f7ec304b217ca")

    assert urls is not None


def test_malware_bazaar():
    urls = malware_bazaar.search("f54093f3b5e316c9092c4bbd107f7ec304b217ca")

    assert urls is not None


def test_polyswarm():
    urls = polyswarm.search("93260b51c4c5a7e05cd398e08af3abaf7aa68c90")

    assert urls is not None


def test_triage():
    urls = triage.search("e9ace713ab91787638a875a72ed8ebd671012bf5")

    assert urls is not None


def test_url_haus():
    urls = url_haus.search("fbe51695e97a45dc61967dc3241a37dc")

    assert urls is not None


def test_virus_bay():
    urls = virus_bay.search("9fbdc5eca123e81571e8966b9b4e4a1e")

    assert urls is not None


def test_virus_share():
    config = load_config()

    if config:
        username, password = config["VirusShare"]["username"], config["VirusShare"]["password"]
        urls = virus_share.search("4c9f110b92d9ba479eb006bb9c81a9c0f1bf44ca", username, password)

        assert urls is not None
    else:
        raise Exception("No config file available to test VirusShare")
