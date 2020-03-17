import unittest

class HomePage(unittest.TestCase):
    #"""description of class"""
    
    def __init__(self):
        print("Home Page Constructor")

    def findTheSearchBox(self, browser):
        self.elem = browser.find_element_by_name('p')  # Find the search box    
        return self.elem

    #@classmethod
    #def tearDownClass(trDwnClass):
    #    trDwnClass.browser.quit()
    #    Print("TestCompleted")


