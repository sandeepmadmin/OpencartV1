import os

import pytest

from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import Loggen

def Test_Login():
    baseurl=ReadConfig.getApplicationURL()
    logger=Loggen.logen()

    user=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("***** Started test_002_loginpage *****")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clicklogin()

        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setpwd(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isMyPageexists()
        if self.targetpage==True:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_login")
            self.driver.close()
            assert False

        self.logger.info("******* End of test_002_login **********")