from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class Uplaod():
    def file_uploading(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/upload')
        time.sleep(4)

        choose_file_btn = driver.find_element(By.ID, 'file-upload')
        choose_file_btn.send_keys("E:\\BITM_Online_14\\Projects\\TestAutomationBITM14\\requirements.txt")

        time.sleep(5)

        upload_btn = driver.find_element(By.ID, 'file-submit')
        upload_btn.click()
        time.sleep(3)

        success_massage = driver.find_element(By.XPATH, '//*[@id="content"]/div/h3')
        success_massage.text
        time.sleep(2)

        driver.close()


obj = Uplaod()
obj.file_uploading()
