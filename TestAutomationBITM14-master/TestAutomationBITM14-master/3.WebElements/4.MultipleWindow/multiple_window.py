from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class MultipleWindow():
    def multiple_window_handle(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/windows')
        time.sleep(4)

        parent_window = driver.current_window_handle
        # print(parent_window)

        driver.find_element(By.LINK_TEXT, 'Click Here').click()

        all_window = driver.window_handles
        # print(all_window)

        # Switch to child
        for child_window in all_window:
            if child_window not in parent_window:
                driver.switch_to.window(child_window)
                time.sleep(5)
                print("Child window title: " + driver.title)

        # Switch to Parent
        for child_window in all_window:
            if child_window not in parent_window:
                driver.switch_to.window(parent_window)
                time.sleep(5)
                print("Parent Window Title: " + driver.title)

        driver.quit()


obj = MultipleWindow()
obj.multiple_window_handle()
