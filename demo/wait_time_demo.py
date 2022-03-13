from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://google.com')
        self.driver.maximize_window()

    def test_sleep(self):
        element = self.driver.find_element(By.NAME,'q')
        element.send_keys('selenium')
        sleep(2) # blocking wait
        element.send_keys(Keys.ENTER)

    def test_implicitly(self):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.NAME,'q')
        element.send_keys('selenium')
        element.send_keys(Keys.ENTER)

    def test_wait(self):
        wait = WebDriverWait(self.driver,2)
        wait.until(EC.title_is('Google'))
        element = self.driver.find_element(By.NAME,'q')
        element.send_keys('selenium')
        element.send_keys(Keys.ENTER)


if __name__ == '__main__':
    case = TestCase()
    case.test_wait()
    case.driver.quit()