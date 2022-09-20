from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


class Browser_Commands():

    def commands(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # open url in browser
        driver.get('https://apple.com')

        # Maximize screen
        driver.maximize_window()

        # full screen
        # driver.fullscreen_window()

        # Get maximize Window side
        maximize_window_size = driver.get_window_size()
        print(maximize_window_size)

        # Set Screen size
        driver.set_window_size(800, 600)

        # delay
        time.sleep(1)

        # get title of current window
        title = driver.title
        print(title)

        # get url of current window
        url = driver.current_url
        print(url)

        # close active window
        driver.close()


obj = Browser_Commands()
obj.commands()
