import time
import pytest
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.MyAccountPage import MyAccountPage
from PageObjects.AccountLogout import AccountLogout
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import Loggen
import os

class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = Loggen.logen()  # Logger

    path = os.path.abspath(os.curdir)+"\\testData\\Opencart_LoginData.xlsx"

    def test_login_ddt(self,setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)  # HomePage Page Object Class
        self.lp = LoginPage(self.driver)  # LoginPage Page Object Class
        self.ma = MyAccountPage(self.driver)  # MyAccount Page Object class
        self.lo = AccountLogout(self.driver) #logout page for continue

        for r in range(2,self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clicklogin()

            self.email=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self.email)
            self.lp.setpwd(self.password)
            time.sleep(3)
            self.lp.clickLogin()
            time.sleep(3)
            self.targetpage=self.lp.isMyPageexists()

            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                    time.sleep(3)
                    self.lo.clickcontinue()
                else:
                    lst_status.append('Fail')
            elif self.exp=='Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                    time.sleep(3)
                    self.lo.clickcontinue()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        #final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of test_003_login_Datadriven **********")
