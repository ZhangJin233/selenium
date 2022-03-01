from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.google.com')
        self.driver.maximize_window()
        sleep(1)
    
    def test_id(self):
        element = self.driver.find_element(By.ID,'kw')
        element.send_keys('selenium')
        print(type(element))


        self.driver.find_element(By.ID,'su').click()
        sleep(1)
        self.driver.quit

    def test_name(self):
        # find_element by.name 方法可能返回多个元素，默认使用第一个
         # find_elements 方法返回多个元素
        element = self.driver.find_element(By.NAME,'q')
        element.send_keys('selenium')

        element.send_keys(Keys.ENTER)
        sleep(1)
        self.driver.quit

    def test_linktext(self):
        self.test_name()
        element = self.driver.find_element(By.LINK_TEXT,'Sign in').click()
        sleep(2)

    def test_partial_link_text(self):
        self.test_name()
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,'Sign').click()
        sleep(2)

    def test_xpath(self):
        element = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        element.send_keys('selenium')
        sleep(2)


    def test_tag_name(self):
        input = self.driver.find_element(By.TAG_NAME,'input')
        print(input)
        sleep(1)
        self.driver.quit

    def test_css_selector(self):
        element = self.driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav.sbfc > div.RNNXgb > div > div.a4bIc > input')
        element.send_keys('selenium')

    def test_class_name(self):
        element = self.driver.find_element(By.CLASS_NAME,'gLFyf gsfi')
        element.send_keys('selenium')

    def test_all(self):
        self.driver.find_element(value='kw').send_keys('selenium')
        



if __name__ == '__main__':
    case = TestCase()
    case.test_class_name()

        

