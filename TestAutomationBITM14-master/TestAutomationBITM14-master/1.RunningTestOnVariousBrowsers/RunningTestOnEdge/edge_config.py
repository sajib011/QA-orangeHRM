from selenium import webdriver

class Edge():
    def edge_launch(self):
        driver = webdriver.Edge(executable_path="\msedgedriver.exe")

    def edge_close(self):
        driver.close()


obj = Edge()
obj.edge_launch()
obj.edge_close()
