import requests


SEARCH_URL = "https://malshare.com/api.php?api_key={}&action=search&query={}"
SAMPLE_URL = "https://malshare.com/sample.php?action=detail&hash={}"


def search(file_hash, api_key):
    r = requests.get(
        SEARCH_URL.format(api_key, file_hash),
        timeout=30
    )
    search_submissions = r.json()
    
    if len(search_submissions) > 0:
        md5 = search_submissions[0]["md5"]
        return SAMPLE_URL.format(md5)

    return None
