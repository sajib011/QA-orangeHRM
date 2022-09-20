from selenium import webdriver

class Firefox():
    def firefox_launch(self):
        driver = webdriver.Chrome(executable_path="\geckodriver.exe")

    def firefox_close(self):
        driver.close()

    def firefox_quit(self):
        driver.quit()


obj = Firefox()
obj.firefox_launch()
obj.firefox_close()