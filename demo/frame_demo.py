from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/framesTest.htm')
        self.driver.maximize_window()

    def test_frame(self):
        top = self.driver.find_element(By.NAME,'top')
        self.driver.switch_to.frame(top)
        self.driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td[1]/a[1]').click()

        self.driver.switch_to.default_content()

        sleep(2)

        second = self.driver.find_element(By.XPATH,'/html/frameset/frame[2]')
        self.driver.switch_to.frame(second)
        self.driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td[1]/a[2]').click()


        




if __name__ == '__main__':
    case = TestCase()
    case.test_frame()
    case.driver.quit()