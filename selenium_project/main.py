from selenium import webdriver
import testcases.testcase1
import testcases.testcase2
from util import util
from testcases.basic.test_user_register import TestUserRegister



if __name__ == "__main__":
    # testcases.testcase1.test()
    # testcases.testcase1.test2()
    # testcases.testcase2.test()
    # driver = webdriver.Chrome()
    # driver.get('http://localhost:8080/jpress/user/register')
    # util.get_coder(driver,'captchaimg')
    case01 = TestUserRegister()
    # case01.test_register_code_error()
    # case01.test_not_fill_username()
    case01.test_register_successful()
