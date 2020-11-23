import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLutils
import time

class Test_001_DDT_Login:    #DDT = Data driven testing

    baseURL = ReadConfig.getApplicationURL()

    path = "/Users/sidmenu/PycharmProjects/nopcommerceApp/testData/LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info(".........TEST 001 LOGIN............")
        self.logger.info("....Verifying homepae title.....")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.act_title = self.driver.title

        if self.act_title == "Your store.. Login":
            assert True
            self.driver.close()
            self.logger.info("Passed")
        else:
            self.driver.save_screenshot("/Users/sidmenu/PycharmProjects/nopcommerceApp/Screenshots"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("Failed")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_DDT(self,setup):

        self.logger.info(".........TEST 001 LOGIN............")
        self.logger.info("....Verifying Login.....")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)

        self.rows = XLutils.getRowCount(Test_001_DDT_Login.path,'Sheet1')
        print("Number of rows in sheet: ",self.rows)

        lst_status=[]

        for r in range(2,self.rows+1):
            self.user = XLutils.readData(Test_001_DDT_Login.path,'Sheet1',r,1)
            self.psd = XLutils.readData(Test_001_DDT_Login.path, 'Sheet1', r, 2)
            self.exp = XLutils.readData(Test_001_DDT_Login.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.psd)
            self.lp.clickLogin()

            time.sleep(5)

            act_title = self.driver.title

            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Passed****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("****Failed****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Failed****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("****Passed****")
                    lst_status.append("Pass")

            if "Fail" not in lst_status:
                self.logger.info("Login DDT passed")
                self.driver.close()
                assert True
            else:
                self.logger.info("Login DDT failed")
                self.driver.close()
                assert False

        self.logger.info("Login test completed")


