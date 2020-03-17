from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class SeleniumWithPythonBase(unittest.TestCase):

    def __init__(self):
        self.driver= webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')   

    #@classmethod
    def setUpClassBase(self):
        self.browser = self.driver        
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()
        return self.browser
          
    @classmethod
    def tearDownClass(trDwnClass):
        trDwnClass.browser.quit()
        Print("TestCompleted")



