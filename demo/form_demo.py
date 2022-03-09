import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path + '/from.html'
        self.driver.get(file_path)

    def test_checkbox(self):
        self.driver.find_element(By.ID,'swimming').click()
        self.driver.find_element(By.ID,'reading').click()
        sleep(2)
        self.driver.quit()

    def test_checkbox2(self):
        swimming = self.driver.find_element(By.ID,'swimming')
        if not swimming.is_selected():
            swimming.click()
        self.driver.find_element(By.ID,'reading').click()
        sleep(2)
        self.driver.quit()

    def test_redio(self):
        list = self.driver.find_element(By.NAME,'gender')
        list[0].click()

if __name__ == '__main__':
    case = TestCase()
    case.test_checkbox()     