from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import Select


class Dropdown(unittest.TestCase):

    def test_dropdown(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/dropdown')

        dropdown = driver.find_element(By.ID, 'dropdown')

        dropdown_values = Select(dropdown)

        # get all option
        for all_options in dropdown_values.options:
            print(all_options.text)

        # dropdown_values.select_by_value('1')
        # dropdown_values.select_by_index(2)
        dropdown_values.select_by_visible_text('Option 1')

        time.sleep(3)

        driver.close()


if __name__ == '__main__':
    unittest.main()





