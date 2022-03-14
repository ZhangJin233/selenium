from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.google.com')
        self.driver.maximize_window()

    def test_js(self):
        self.driver.execute_script("alert('test')")
        sleep(2)
        self.driver.switch_to.alert.accept()

    def test_execute_js(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)

    def test_execute_js2(self):
        js = 'var q = document.getElementByName("q"); q.style.border="2px solid red"'
        self.driver.execute_script(js)
        sleep(2)

    def test_execute_js3(self):
        element = self.driver.find_element(By.NAME,'q')
        element.send_keys('selenium')
        element.send_keys(Keys.ENTER)
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(2)

if __name__ == '__main__':
    case = TestCase()
    case.test_execute_js3()
    case.driver.quit()
        