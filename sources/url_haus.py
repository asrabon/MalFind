import requests

from bs4 import BeautifulSoup

SEARCH_URL = 'https://urlhaus.abuse.ch/browse.php?search={}'
ROOT_URL = "https://urlhaus.abuse.ch"

def search(file_hash):
    urls = []
    r = requests.get(
        SEARCH_URL.format(file_hash),
        timeout=30
    )
    
    search_result = r.text

    soup = BeautifulSoup(search_result, "html.parser")
    sample_trs = soup.find("table").find_all("tr")[1:]
    
    if sample_trs:
        for tr in sample_trs:
            sample_id = tr.find('a')['href'] 
            urls.append("{}{}".format(ROOT_URL, sample_id))
    else:
        return None

    return urls
