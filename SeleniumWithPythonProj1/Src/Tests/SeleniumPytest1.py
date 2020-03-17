import unittest
import sys  #**********Below three imports/statments are useful to import relative classes in multi folder structure
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Src.Pages.HomePage import HomePage
from Src.Tests.SeleniumWithPythonBase import SeleniumWithPythonBase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner
import io


class Test_SeleniumPytest1(unittest.TestCase):
    
      @classmethod
      def setUpClass(cls):
          print("this is setup class function, runs once for the class not for each test")

      def setUp(self):
        self.widget = 'The widget'
        print(self.widget)
    
      def test_IsYahooSearchWorking(self):                    
          driver = SeleniumWithPythonBase()          
          browser = driver.setUpClassBase()  
          browser.get('http://www.yahoo.com')
          assert 'Yahoo' in browser.title
          #elem = browser.find_element_by_name('p')  # Find the search box
          HomePage_obj = HomePage()
          searchElement = HomePage_obj.findTheSearchBox(browser)
          searchElement.send_keys('seleniumhq' + Keys.RETURN)
          browser.implicitly_wait(1)
          #objOfThisClass = Test_SeleniumPytest1(); Create the object to call the self class functions
          #objOfThisClass.tearDownClassone(browser)

      @unittest.skip("demonistrating skipping")
      def test_nothing(self):
           driver = SeleniumWithPythonBase()          
           browser = driver.setUpClassBase()
           self.fail("Shouldn't happened")

    #@unittest.skip("demonstrating skipping")
      def test_nothingTwo(self):
        self.tnow = time.asctime()
        print(self.tnow)
        self.fail("shouldn't happen")
       
        #@unittest.skip("demonstrating skipping")
      def test_nothingThree(self):
        self.tnow = time.asctime()
        print(self.tnow)
        self.fail("test_nothingThree shouldn't happen")

   # @classmethod
      def tearDownClassone(self, browserDriver):
        # browser.close() closes only one browser which is active
        browserDriver.quit() # Closes all browsers opend by this instance of webdriver
        print("TestCompleted")

        def tearDown(self, browserDriver):
            # browser.close() closes only one browser which is active
              print("TestCompleted")
              print("In TearDown")
              browserDriver.quit() # Closes all browsers opend by this instance of webdriver
    
      @classmethod
      def tearDownClass(cls):
          print("this is class level teardown function runs once per class not for every test")
     
      def smokeTests(self):
        self.smokeTests = unittest.TestSuite()
        self.smokeTests.addTest(Test_SeleniumPytest1('test_IsYahooSearchWorking'))
        self.smokeTests.addTest(Test_SeleniumPytest1('test_nothingTwo'))
        self.smokeTests.addTest(Test_SeleniumPytest1('test_nothingThree'))
        return self.smokeTests      
             #self.widget.dispose()

      def regressionTests():
        regressionTests = unittest.TestSuite()
        #regressionTests.addTest(Test_SeleniumPytest1('test_setUpClassone'))
        regressionTests.addTest(Test_SeleniumPytest1('test_nothingThree'))
        return regressionTests 
    
    #*******************************This is very useful************************
#if __name__ == '__main__':
#    runner = unittest.TextTestRunner()
#    objOfThisClass = Test_SeleniumPytest1();
#    runner.run(objOfThisClass.smokeTests())
#    #unittest.main()
    #**************************************************************************

    #******************************This is the way to run the tests using HTML runner*************
if __name__ == '__main__':
    #runner = unittest.TextTestRunner()
    objOfThisClass = Test_SeleniumPytest1();
    suite = objOfThisClass.smokeTests()
    #runner.run(objOfThisClass.smokeTests())
    #unittest.main()
    outfile=open("D:\\TestReport.html", "w")    
    runner = HtmlTestRunner.HTMLTestRunner(output='D:\\TestReport')
    #runner = HtmlTestRunner.HTMLTestRunner(
    #    stream=outfile,
    #    verbosity=1    
    #    )
    runner.run(suite)

#runner.run(suite)
    #**********************************************************************************************
    # cd into project directory and run the command "python class file name" to run only above grouped tests
    #Example D:\TestProjects\SeleniumWithPythonProj1\SeleniumWithPythonProj1>python SeleniumPytest1.py
    # Python docs for unit testing https://docs.python.org/3/library/unittest.html

    # To run all test we can do this 
    # C:\Users\GuestGuest>python -m unittest discover "D:\\TestProjects\\SeleniumWithPythonProj1\\SeleniumWithPythonProj1" "SeleniumPytest1.py"
    # and the Main function can be like this
    # if __name__ == '__main__':
    #unittest.main()

    # To generate PyTest reports run this command "D:\TestProjects\SeleniumWithPythonProj1\SeleniumWithPythonProj1\Src\Tests>pytest -v SeleniumPytest1.py --html=pytest_report.html --self-contained-html"
    #CMD to run the tests while using "HTMLTestRunner" is "D:\TestProjects\SeleniumWithPythonProj1\SeleniumWithPythonProj1\Src\Tests>python SeleniumPytest1.py" and works with below import statments only
    #import sys  
    #import os
    #sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))