import requests
from requests.exceptions import ConnectionError
from urllib.error import HTTPError, URLError
import bs4

# creating a user defined function to check the errors before web scrapping


class UrlError:
    def __init__(self, url: str) -> None:
        self.url = url

    def urlopen(self) -> bool:
        try:
            var = "NoError"
            read = requests.get(self.url)
            # requests.sessions().close()
        except HTTPError as e:
            var = "HTTPError"
        except URLError as e:
            var = "URLError"
        except ConnectionError as e:
            var = "ConnectionError"
        if var == "NoError":
            return read, read.status_code, True
        else:
            return None, var, False

    def parser(self) -> str:
        read, status, error = self.urlopen()
        if error:
            return bs4.BeautifulSoup(read.text, 'lxml')
        else:
            return "Error while occuring with code "+status
