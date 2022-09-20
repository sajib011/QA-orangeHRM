import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from Framework.pages.login_page import LoginPage
from Framework.pages.myinfo_ec_page import MyInfoPage
from Framework.utils import excel_utils
import logging


class MyinfoTest(unittest.TestCase):

    def test_ec_add(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        # Implement login
        lp = LoginPage(driver)
        lp.login_orange("Admin", "admin123")

        # implement My info
        mi = MyInfoPage(driver)
        mi.emergency_contract_add("Test Name", "Brother", "123456")

        driver.close()
