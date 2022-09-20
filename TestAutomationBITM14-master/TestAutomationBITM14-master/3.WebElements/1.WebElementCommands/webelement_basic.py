# Commands:
# 1. Click
# 2. Type
# 3. clear
# 4. text
# 5. size
# 6. state of Elements

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import unittest


class WebElements(unittest.TestCase):

    def basic_commands(self):
        # launch Firefox
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()

        # open url in browser
        driver.get('https://opensource-demo.orangehrmlive.com/')

        # Locate webelements
        username = driver.find_element(By.ID, 'txtUsername')
        password = driver.find_element(By.ID, 'txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Text
        forgot_password = driver.find_element(By.LINK_TEXT, 'Forgot your password?')
        print(forgot_password.text)

        # Size
        size_username = username.size
        print(size_username)
        print('Width is:' + str(size_username['width']))
        print('Height is:' + str(size_username['height']))

        self.assertEqual(232, size_username['width'], 'Error')
        self.assertEqual(16, size_username['height'], 'error')

        # sate
        username_display_sate = username.is_displayed()  # True
        # print(username_display_sate)
        self.assertEqual(True, username_display_sate, "Username hide.Test failed.")

        username_enable_state = username.is_enabled()
        # print(username_enable_state)
        self.assertEqual(True, username_enable_state, "Username disabled,Test failed.")

        # Login Action
        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        time.sleep(5)

        # Element state
        driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
        time.sleep(5)
        agree = driver.find_element(By.NAME, 'agree')
        agree_selected_state = agree.is_selected()  # True or False
        self.assertEqual(False, agree_selected_state, "Already selected.Test Failed.")

        # close
        driver.close()


obj = WebElements()
obj.basic_commands()
