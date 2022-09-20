from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


class Navigate():
    def navigate_demo(self):
        # launch Firefox
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # open url in browser
        driver.get('https://apple.com')

        # open url in browser
        driver.get('https://google.com')
        time.sleep(2)

        # back
        driver.back()  # Apple
        time.sleep(3)

        # forward
        driver.forward()  # Google
        time.sleep(3)

        # reload/refresh
        driver.refresh()
        time.sleep(3)

        # Open new tab
        driver.switch_to.new_window('window2')
        time.sleep(2)

        # Open new window
        driver.switch_to.new_window('window3')
        driver.get("https://www.apple.com/iphone/")
        time.sleep(3)

        # close
        driver.close()


obj = Navigate()
obj.navigate_demo()
