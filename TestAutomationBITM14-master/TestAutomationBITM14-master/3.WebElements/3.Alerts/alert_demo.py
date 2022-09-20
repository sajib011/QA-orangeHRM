from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class Alert():
    def alert_automation(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/javascript_alerts')

        # Normal Alert
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button').click()
        driver.switch_to.alert.accept()  # Clicked on OK
        time.sleep(5)

        # Confirmation Alert
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click()
        driver.switch_to.alert.dismiss()  # Clicked on Cancel
        time.sleep(3)

        # Prompt Alert
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
        driver.switch_to.alert.send_keys('Test Automation')
        driver.switch_to.alert.accept()
        time.sleep(3)

        driver.close()


obj = Alert()
obj.alert_automation()
