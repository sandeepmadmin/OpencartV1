from selenium.webdriver.common.by import By

class MyAccountPage:

    lnk_logout_xpath="//a[@class='dropdown-item' and text()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.lnk_logout_xpath).click()

