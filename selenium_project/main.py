from selenium import webdriver
import testcases.testcase1
import testcases.testcase2
from util import util
from testcases.basic.test_user_register import TestUserRegister
from testcases.basic.test_user_login import TestUserLogin
from testcases.basic.test_admin_login import TestAdminLogin




if __name__ == "__main__":
    # testcases.testcase1.test()
    # testcases.testcase1.test2()
    # testcases.testcase2.test()
    # driver = webdriver.Chrome()
    # driver.get('http://localhost:8080/jpress/user/register')
    # util.get_coder(driver,'captchaimg')
    # case01 = TestUserLogin()
    case01 = TestAdminLogin()

    # case01.test_register_code_error()
    # case01.test_not_fill_username()
    # case01.test_user_login_with_username_error()
    # case01.test_not_fill_password()
    # case01.test_login_success()
    case01.test_fill_nothing_in_username()
    case01.test_fill_nothing_in_password()
    case01.test_login_with_error_code()
