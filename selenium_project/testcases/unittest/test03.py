import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls)->None:
        print('setupClass')
        cls.driver = webdriver.Chrome()
        cls.driver.get('')
        cls.driver.maximize_window()

    def setUp(self)->None:
        print('setup')

    def tearDown(self)->None:
        print('tearDown')



    @classmethod
    def tearDownClass(cls)-> None:
        print('tearDownClass')
        cls.driver.quit()

    def tearDown(self)-> None:
        print('tearDown')

if __name__ == '__main__':
    unittest.main()


