from selenium.webdriver.common.by import By

class AccountRegistrationPage():

    txt_firstname_name="firstname"
    txt_lastname_name="lastname"
    txt_email_name="email"
    txt_password_name="password"
    chk_policyagree_name="agree"
    btn_continue_xpath = "//button[text()='Continue']"
    txt_msg_cnf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self,driver):
        self.driver = driver

    def setfirstname(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setlastname(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setemail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def setpassword(self,pwd):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)

    def setPrivacypolicy(self):
        self.driver.find_element(By.NAME,self.chk_policyagree_name).click()

    def clickcontinue(self):
        self.driver.find_element(By.XPATH,self.btn_continue_xpath).click()

    def getconfirmation(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_msg_cnf_xpath).text
        except:
            None