from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestUserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls)-> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:8080/jpress/user/login')
        cls.driver.maximize_window()

    def test_user_login_with_username_error(self):
        username = 'username'
        password = 'pwd'
        expected = '用户名不正确。'
        self.driver.find_element(By.NAME,'user').send_keys(username)
        self.driver.find_element(By.NAME,'pwd').send_keys(password)
        self.driver.find_element(By.CLASS_NAME,'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == expected
        alert.accept()

    def test_not_fill_password(self):
        username = 'username'
        expected = '密码不能为空'
        self.driver.find_element(By.NAME,'user').clear()
        self.driver.find_element(By.NAME,'pwd').clear()
        self.driver.find_element(By.NAME,'user').send_keys(username)
        self.driver.find_element(By.CLASS_NAME,'btn').click()
        
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == expected
        alert.accept()

    def test_login_success(self):
        username = 'test'
        password = '123456'
        expected = '用户中心'

        self.driver.find_element(By.NAME,'user').clear()
        self.driver.find_element(By.NAME,'pwd').clear()
        self.driver.find_element(By.NAME,'user').send_keys(username)
        self.driver.find_element(By.NAME,'pwd').send_keys(password)
        self.driver.find_element(By.CLASS_NAME,'btn').click()


        WebDriverWait(self.driver, 5).until(EC.title_is(expected))

        assert self.driver.title == expected

if __name__ == '__main__':
    unittest.main()






    