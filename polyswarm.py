import requests

SEARCH_MD5_URL = 'https://portal-backend.k.polyswarm.network/api/v1/submission/hash/md5/{}'
SEARCH_SHA1_URL = 'https://portal-backend.k.polyswarm.network/api/v1/submission/hash/sha1/{}'
SEARCH_SHA256_URL = 'https://portal-backend.k.polyswarm.network/api/v1/submission/hash/sha256/{}'
SAMPLE_URL = "https://polyswarm.network/scan/results/file/{}/details"

def search(file_hash):
    if len(file_hash) == 32:
        search_url = SEARCH_MD5_URL
    elif len(file_hash) == 40:
        search_url = SEARCH_SHA1_URL
    else:
        search_url = SEARCH_SHA256_URL

    r = requests.get(
        search_url.format(file_hash),
        timeout=30
    )
    
    search_result = r.json()

    if r.status_code == 200:
        return SAMPLE_URL.format(
            search_result["result"]["sha256"]
        )
    else:
        return None
