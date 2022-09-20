from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class Screenshot():
    def capture_screenshot(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://google.com/')
        time.sleep(4)

        driver.get_screenshot_as_file('E:\\BITM_Online_14\\Projects\\TestAutomationBITM14\\3.WebElements\\Screenshots\\ScreenshotFiles\\image.png')

        driver.close()


obj = Screenshot()
obj.capture_screenshot()