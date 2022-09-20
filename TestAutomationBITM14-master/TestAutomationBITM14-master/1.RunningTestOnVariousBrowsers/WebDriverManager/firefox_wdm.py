from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class Firefox_WDM():
    def firefox_launch(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


obj = Firefox_WDM()
obj.firefox_launch()