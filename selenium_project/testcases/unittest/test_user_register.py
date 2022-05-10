from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import util
from lib.HTMLTestRunner import HTMLTestRunner
import unittest

class TestUserRegister(unittest.TestCase):
    def setUpClass(cls)->None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:8080/jpress/user/register')
        cls.driver.maximize_window()

    def test_register_code_error(self):
        id = 'test'
        email = 'test@example.com'
        password = 'test'
        confirmpassword = 'test'
        captcha = 'test'
        expected = '验证码不正确'

        self.driver.find_element(By.NAME,'username').send_keys(id)
        self.driver.find_element(By.NAME,'email').send_keys(email)
        self.driver.find_element(By.NAME,'pwd').send_keys(password)
        self.driver.find_element(By.NAME,'confirmPwd').send_keys(confirmpassword)
        self.driver.find_element(By.NAME,'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME,'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == expected
        alert.accept()

    def test_not_fill_username(self):
        expected = '用户名不能为空'
        self.driver.find_element(By.NAME,'username').send_keys(' ')
        self.driver.find_element(By.CLASS_NAME,'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == expected
        alert.accept()


    def test_register_successful(self):
        id = 'test'
        email = 'test@example.com'
        password = '123456'
        confirmpassword = '123456'
        captcha = util.get_coder(self.driver,'captchaimg')
        expected = '注册成功，点击确定进行登录'

        self.driver.find_element(By.NAME,'username').send_keys(id)
        self.driver.find_element(By.NAME,'email').send_keys(email)
        self.driver.find_element(By.NAME,'pwd').send_keys(password)
        self.driver.find_element(By.NAME,'confirmPwd').send_keys(confirmpassword)
        captcha = util.get_coder(self.driver,'captchaimg')

        self.driver.find_element(By.NAME,'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME,'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == expected
        alert.accept()

    def runTest(self):
        self.test1_register_code_error()
        self.test2_register_ok()

if __name__ == '__main__':

    suite = unittest.TestSuite()


    # 方法一： 通过测试用例类进行加载
    suite.addTest(TestUserRegister("test2_register_ok"))

    fp = open(r"./result.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="test register", description="用例执行情况")
    runner.run(suite)
    runner.generateReport()
    fp.close()




