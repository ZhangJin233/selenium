import os
from time import localtime, strftime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.google.com')
        self.driver.maximize_window()

    def test_screenshot(self):
        element = self.driver.find_element(By.NAME,'q')
        element.send_keys('selenium')
        element.send_keys(Keys.ENTER)
        st = strftime("%Y-%m-%d-%H-%M-%S",localtime(time()))
        file_name = st + '.png'
        path = os.path.abspath('screenshot')
        file_path = path + '/' + file_name
        # self.driver.save_screenshot(file_name)
        self.driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    case = TestCase()
    case.test_screenshot()
    case.driver.quit()