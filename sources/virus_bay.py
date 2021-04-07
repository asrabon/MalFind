import requests

from fake_useragent import UserAgent


SEARCH_URL = "https://beta.virusbay.io/sample/search?q={}"
BROWSE_URL = "https://beta.virusbay.io/sample/browse?q={}"


def search(file_hash):
    ua = UserAgent()
    r = requests.get(
        SEARCH_URL.format(file_hash),
        headers={
            'User-Agent': ua.random,
            'Host': 'beta.virusbay.io'
        },
        timeout=30
    )
    search_submissions = r.json()
    
    if "search" in search_submissions and len(search_submissions) > 0:
        return BROWSE_URL.format(file_hash)

    return None
