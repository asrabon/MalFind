import requests

from bs4 import BeautifulSoup

SEARCH_URL = 'https://tria.ge/s?q={}'
ROOT_URL = "https://tria.ge"

def search(file_hash):
    urls = []
    r = requests.get(
        SEARCH_URL.format(file_hash),
        timeout=30
    )
    
    search_result = r.text

    if "No reports found." in search_result:
        return None
    else:
        soup = BeautifulSoup(search_result, "html.parser")
        sample_trs = soup.find("table").find_all("tr")[1:]
        
        for tr in sample_trs:
            sample_id = tr.find('a')['href'] 
            urls.append("{}{}".format(ROOT_URL, sample_id))

        return urls
