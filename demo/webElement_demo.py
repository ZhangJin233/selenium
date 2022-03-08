from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement



class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.get('http://google.com')
        self.driver.get('http://sahitest.com/demo/linkTest.htm')
        self.driver.maximize_window()

    def test_prop(self):
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.page_source)
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.quit

    def test_webdriver_prop(self):
        e = self.driver.find_element(By.ID,'t1')
        e1 = WebElement
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.rect)
        print(e.text)

    def test_webelement_method(self):
        e = self.driver.find_element(By.ID,'t1')
        e.send_keys('hello world')
        sleep(2)
        

        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))

        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))

        sleep(2)
        e.clear()

    def test_window(self):
        self.driver.find_element(By.LINK_TEXT,'linkByContent').click()
        window = self.driver.window_handles

        while True:
            for i in window:
                self.driver.switch_to.window(i)
                sleep(2)



if __name__ == '__main__':
    case = TestCase()
    case.test_window()