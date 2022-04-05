import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):

    def setUp(self)->None:
        print('setup')

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://google.com')
        cls.driver.maximize_window()
        # super().setUpClass()

    def test01(self):
        print('test01')
        element = self.driver.find_element(By.NAME,'q')
        element.send_keys('selenium')

    def test02(self):
        print('test02')
        self.assertLess(1,2)
        self.assertGreater(2, 1)
        self.assertIn(10,[1,2,3])

    def tearDown(self)->None:
        print('tearDown')

    @classmethod
    def tearDownClass(cls)->None:
        print('tearDownClass')
        cls.driver.quit()
        # super().tearDownClass()


if __name__ == '__main__':
    unittest.main()