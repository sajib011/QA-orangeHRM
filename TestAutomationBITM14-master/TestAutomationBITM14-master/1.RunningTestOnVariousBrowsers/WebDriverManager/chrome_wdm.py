from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Chrome_WDM():
    def chrome_config(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


obj = Chrome_WDM()
obj.chrome_config()