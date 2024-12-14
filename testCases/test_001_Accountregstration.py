#Below is my code
import pytest
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.HomePage import HomePage
from PageObjects.AcountregstationPage import AccountRegistrationPage
from utilities.randomString import randomstringgen
from selenium.webdriver.common.by import By
import time
import os

from utilities.readProperties import ReadConfig

from utilities.customLogger import Loggen # for logging


class Test_001_AccountReg:
    base_url = ReadConfig.getApplicationURL()
    logger=Loggen.logen()# for logging

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("**** test_001_Accountregstration started ****")
        self.driver= setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.logger.info("Clicking on My Account-->Register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("Providing customer details for registration")
        self.reg=AccountRegistrationPage(self.driver)

        self.reg.setfirstname("John")
        self.reg.setlastname("Scott")
        self.email=randomstringgen() + '@gmail.com'
        self.reg.setemail(self.email)
        # self.reg.setemail("Test01")#test for failure case by giving invalid email
        self.reg.setpassword("Test@123")
        time.sleep(5)
        #self.policy = self.driver.find_element(By.NAME, "agree")
        #self.driver.execute_script("arguments[0].scrollIntoView();",self.policy)
        self.driver.execute_script("window.scrollBy(0, document.documentElement.scrollHeight);")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "agree")))
        self.reg.setPrivacypolicy()
        time.sleep(5)
        #self.cont= self.driver.find_element(By.XPATH,"//button[text()='Continue']")
        #self.driver.execute_script("arguments[0].scrollIntoView();",self.cont)
        self.driver.execute_script("window.scrollBy(0, document.documentElement.scrollHeight);")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
        self.reg.clickcontinue()
        time.sleep(5)
        self.confmsg=self.reg.getconfirmation()
        self.driver.close()
        if self.confmsg == 'Your Account Has Been Created!':
            self.logger.info("Account registration passed")
            assert True
        else:
            #self.driver.save_screenshot(os.path.join(os.path.abspath(os.curdir), "screenshots", "test_account_reg.png"))#chat gpt
            self.logger.error("Account registration failed")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png")
            #always save screenshot with method name to keep track
            assert False

        self.logger.info("**** test_001_Accountregstration finished ****")

