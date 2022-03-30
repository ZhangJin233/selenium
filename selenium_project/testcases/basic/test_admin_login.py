from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import util


class TestAdminLogin(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.maximize_window()

    def test_fill_nothing_in_username(self):
        password = '123456'
        code = '6666'
        expected = '账号不能为空'

        self.driver.find_element(By.NAME,'user').clear()
        self.driver.find_element(By.NAME,'pwd').clear()
        self.driver.find_element(By.NAME,'pwd').send_keys(password)
        self.driver.find_element(By.NAME,'captcha').send_keys(code)
        self.driver.find_element(By.CLASS_NAME,'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        alert = self.driver.switch_to.alert

        assert alert.text == expected

        alert.accept()

    def test_fill_nothing_in_password(self):
        username = 'admin'
        code = '6666'
        expected = '密码不能为空'

        self.driver.find_element(By.NAME,'user').clear()
        self.driver.find_element(By.NAME,'pwd').clear()
        self.driver.find_element(By.NAME,'captcha').clear()
        self.driver.find_element(By.NAME,'user').send_keys(username)
        self.driver.find_element(By.NAME,'captcha').send_keys(code)
        self.driver.find_element(By.CLASS_NAME,'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        alert = self.driver.switch_to.alert

        assert alert.text == expected

        alert.accept()

    def test_login_with_error_code(self):
        username = 'admin'
        password = '123456'
        code = '6666'
        expected = '验证码不正确，请重新输入'

        self.driver.find_element(By.NAME,'user').clear()
        self.driver.find_element(By.NAME,'pwd').clear()
        self.driver.find_element(By.NAME,'captcha').clear()
        self.driver.find_element(By.NAME,'user').send_keys(username)
        self.driver.find_element(By.NAME,'pwd').send_keys(password)
        self.driver.find_element(By.NAME,'captcha').send_keys(code)
        self.driver.find_element(By.CLASS_NAME,'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        alert = self.driver.switch_to.alert

        assert alert.text == expected

        alert.accept()

