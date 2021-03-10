import requests

SEARCH_URL = 'https://malquarium.org/api/query/{}/'
SAMPLE_URL = "https://malquarium.org/samples/{}"

def search(file_hash):
    r = requests.get(
        SEARCH_URL.format(file_hash),
        timeout=30
    )

    search_result = r.json()
    if len(search_result["results"]) > 0:
        sha256 = search_result["results"][0]["sha2"]
        return SAMPLE_URL.format(sha256)
    return None
