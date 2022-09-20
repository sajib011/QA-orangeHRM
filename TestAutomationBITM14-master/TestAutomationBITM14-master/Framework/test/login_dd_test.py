import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from Framework.pages.login_page import LoginPage
from Framework.utils import excel_utils

# Read data and implementing in test


class LoginTest(unittest.TestCase):

    def test_dd_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        # Excel Implement
        file = "E:\\BITM_Online_14\\Projects\\TestAutomationBITM14\\Framework\\data\\login_data.xlsx"
        sheet = "Sheet1"

        number_of_rows = excel_utils.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            username_data = excel_utils.read_data(file, sheet, r, 1)
            password_data = excel_utils.read_data(file, sheet, r, 2)

            lp = LoginPage(driver)
            lp.login_orange(username_data, password_data)

        driver.close()
