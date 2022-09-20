from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Edge_WDM():
    def edge_config(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


obj = Edge_WDM()
obj.edge_config()
