import os
from pyvirtualdisplay.display import Display

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from .engine import Engine


class Core():

    def __init__(self, engine: Engine, driver_path: str) -> None:
        Display(visible=False, size=(1920, 1080)).start()
        self.driver = webdriver.Firefox(service=FirefoxService(driver_path, log_path=os.devnull)) if engine == Engine.firefox \
                      else (webdriver.Chrome(service=ChromeService(driver_path, log_path=os.devnull)) if engine == Engine.chrome \
                      else webdriver.Edge(service=EdgeService(driver_path, log_path=os.devnull)))

    def go_to_url(self, url: str) -> None:
        self.driver.get(url)

    def get_url_title(self) -> str:
        return self.driver.title

    def close(self) -> None:
        self.driver.quit()
