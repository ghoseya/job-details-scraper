from requests import get
from requests.exceptions import ConnectionError
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

# creating a user defined function to check the errors before web scrapping


class UrlParseBs:
    def __init__(self, url: str) -> None:
        self.url = url

    def urlopen(self): # Returns 3 values
        try:
            var = "NoError"
            read = get(self.url)
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
            return BeautifulSoup(read.text, 'lxml')
        else:
            return "Error while occuring with code "+status

from selenium import webdriver
from time import sleep
from selenium.common.exceptions import WebDriverException
from os import curdir
from os.path import join, abspath

class UrlParseSe:
    def __init__(self, url: str) -> None:
        self.url = url
    
    def urlopen(self):
        try:
            var = "NoError"
            read = get(self.url)
            # requests.sessions().close()
        except HTTPError as e:
            var = "HTTPError"
        except URLError as e:
            var = "URLError"
        except ConnectionError as e:
            var = "ConnectionError"
        if var == "NoError":
            return read.status_code, True 
        else:
            return var, False
    
    def parse(self) -> str:
        status, error = self.urlopen()
        if error:
            try:
                driver = webdriver.Firefox()
            except WebDriverException as e:
                print("Firefox Driver not installed properly\nCustom Driver Setted up\n> Driver: mozilla/geckodriver\n> version:0.30.0\n")
                exec_path = join(abspath(curdir), 'Drivers', 'geckodriver')
                driver = webdriver.Firefox(executable_path=exec_path)
            except:
                return "Firefox Driver Not installed"
            driver.get(self.url)
            sleep(20)
            source = driver.page_source
            driver.quit()
            return BeautifulSoup(source, 'lxml')
        else:
            return "Error while occuring with code "+status
