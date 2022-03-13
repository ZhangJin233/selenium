from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.get('http://sahitest.com/demo/alertTest.htm')
        # self.driver.get('http://sahitest.com/demo/confirmTest.htm')
        self.driver.get('http://sahitest.com/demo/promptTest.htm')
        self.driver.maximize_window()

    def test_alert(self):
        self.driver.find_element(By.NAME,'b1').click()
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element(By.NAME,'b1').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        confirm.accept()

    def test_prompt(self):
        self.driver.find_element(By.NAME,'b1').click()
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        sleep(3)
        prompt.send_keys('1111111')
        sleep(3)
        prompt.accept()
        sleep(3)



if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    case.test_prompt()
    case.driver.quit()