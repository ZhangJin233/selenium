from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/waitFor.htm')
        self.driver.maximize_window()

    def test_wait_for(self):
        self.driver.find_element(By.XPATH,'/html/body/form/input[2]').click()
        wait = WebDriverWait(self.driver,3)
        wait.until(EC.text_to_be_present_in_element(By.XPATH,'//*[@id="id2"]'),'id 2')
        print('ok')
        

if __name__ == '__main__':
    case = TestCase()
    case.test_wait_for()
    case.driver.quit()
