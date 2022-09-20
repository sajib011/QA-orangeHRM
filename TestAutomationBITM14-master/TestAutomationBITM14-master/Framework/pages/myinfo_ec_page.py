import time
from selenium.webdriver.common.by import By

class MyInfoPage():

    def __init__(self, driver):
        self.driver = driver

    def emergency_contract_add(self, name, relationship, telephone):
        # Open my info page
        my_info = self.driver.find_element(By.LINK_TEXT, 'My Info')
        my_info.click()

        # Open Emergency Contract
        emergency_contract = self.driver.find_element(By.LINK_TEXT, 'Emergency Contacts')
        emergency_contract.click()
        time.sleep(2)

        add_btn = self.driver.find_element(By.ID, 'btnAddContact')
        add_btn.click()

        name_field = self.driver.find_element(By.ID, 'emgcontacts_name')
        name_field.send_keys(name)

        relationship_field = self.driver.find_element(By.ID, 'emgcontacts_relationship')
        relationship_field.send_keys(relationship)

        telephone_field = self.driver.find_element(By.ID, 'emgcontacts_homePhone')
        telephone_field.send_keys(telephone)

        save = self.driver.find_element(By.ID, 'btnSaveEContact')
        save.click()




