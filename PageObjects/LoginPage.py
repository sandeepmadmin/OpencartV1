from selenium.webdriver.common.by import By

class LoginPage:
    txt_email_xpath="//input[@id='input-email']"
    txt_pwd_xpath="//input[@id='input-password']"
    btn_login_xpath="//button[text()='Login']"
    msg_myaccount_xpath="//h2[text()='My Account']"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def setpwd(self,password):
        self.driver.find_element(By.XPATH,self.txt_pwd_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def isMyPageexists(self):
        try:
            self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).is_displayed()
        except:
            return False