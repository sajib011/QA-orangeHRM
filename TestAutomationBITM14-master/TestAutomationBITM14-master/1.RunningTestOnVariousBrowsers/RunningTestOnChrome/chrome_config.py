from selenium import webdriver

class Chrome():

    def chrome_launch(self):
        driver = webdriver.Chrome(executable_path="\chromedriver.exe")

    def chrome_close(self):
        driver.close()


obj = Chrome()
obj.chrome_launch()
obj.chrome_close()