import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from Framework.pages.login_page import LoginPage


class LoginTest(unittest.TestCase):

    def test_valid_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(3)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        lp = LoginPage(driver)
        lp.login_orange("Admin", "admin123")

        driver.close()

    def test_Invalid_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(3)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        lp = LoginPage(driver)
        lp.login_orange("Admin3432432", "admin123")

        driver.close()
