from selenium.webdriver.common.by import By

class AccountLogout:
    lnk_continue_xpath="//a[text()='Continue']"

    def __init__(self,driver):
        self.driver=driver
    def clickcontinue(self):
        self.driver.find_element(By.XPATH,self.lnk_continue_xpath).click()