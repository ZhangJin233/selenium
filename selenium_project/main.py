from selenium import webdriver
import testcases.testcase1
import testcases.testcase2
from util import util



if __name__ == "__main__":
    # testcases.testcase1.test()
    # testcases.testcase1.test2()
    # testcases.testcase2.test()
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/jpress/user/register')
    util.get_coder(driver,'//*[@id="captchaimg"]')