import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent


LOGIN_URL = "https://virusshare.com/processlogin"
SEARCH_URL = "https://virusshare.com/search"
ROOT_URL = "https://virusshare.com/"


def search(file_hash, username, password):
    ua = UserAgent()
    s = requests.session()

    r = s.post(
        LOGIN_URL,
        headers={
            'User-Agent': ua.random,
        },
        data = {
            "username": username,
            "password": password
        },
        timeout=30
    )

    r = s.post(
        SEARCH_URL,
        headers={
            'User-Agent': ua.random,
        },
        data = {
            "search": file_hash,
        },
        timeout=30
    )

    try:
        soup = BeautifulSoup(r.text, "html.parser")
        url = soup.find('a', {'title' : 'Link to this report'})['href'] 

        return ROOT_URL + url
    except:
        pass

    return None
