from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from Test_Data import data
from Test_Locators import locators

class Test_Kavitha:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()
        


    def test_login_TC_PIM_01(self, booting_function):
        self.driver.get(data.Data().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(data.Data().username)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().forgot_password).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().username_text).send_keys(data.Data().resetusername)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().reset_password).click()
        sleep(5)
        resetmsg=self.driver.find_element(by=By.XPATH, value=locators.Locators().variable).text
        sleep(5)
        assert resetmsg == data.Data().result



    def test_loginadmin_TC_PIM_02(self, booting_function):
        self.driver.get(data.Data().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(data.Data().username)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).send_keys(data.Data().password)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().submit_button).click()
        sleep(5)
        assert self.driver.title == 'OrangeHRM'
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().admin).click()
        sleep(5)
        User_Management=self.driver.find_element(by=By.XPATH, value=locators.Locators().usermanagement)
        sleep(5)
        print("display status:",User_Management.is_displayed())
        Job=self.driver.find_element(by=By.XPATH, value=locators.Locators().job)
        sleep(5)
        print("display status:",Job.is_displayed())
        Organisation=self.driver.find_element(by=By.XPATH, value=locators.Locators().organisation)
        sleep(5)
        print("display status:",Organisation.is_displayed())
        Qualifications=self.driver.find_element(by=By.XPATH, value=locators.Locators().qualifications)
        sleep(5)
        print("display status:", Qualifications.is_displayed())
        Nationalities=self.driver.find_element(by=By.XPATH, value=locators.Locators().nationalities)
        sleep(5)
        print("display status:",Nationalities.is_displayed())
        Corporate_Branding=self.driver.find_element(by=By.XPATH, value=locators.Locators().corporatebranding)
        sleep(5)
        print("display status:",Corporate_Branding.is_displayed())
        Configuration=self.driver.find_element(by=By.XPATH, value=locators.Locators().configuration)
        sleep(5)
        print("display status:",Configuration.is_displayed())
        sleep(5)

        options=self.driver.find_elements(by=By.CLASS_NAME, value=locators.Locators().option)

        for opt in options:
            print(opt.text)
            assert opt.is_displayed()
        
    def test_loginadmin_TC_PIM_03(self, booting_function):
        self.driver.get(data.Data().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(data.Data().username)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).send_keys(data.Data().password)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().submit_button).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().admin).click()
        sleep(5)

        sideoptions=self.driver.find_elements(by=By.CLASS_NAME, value=locators.Locators().sideoption)

        for sopt in sideoptions:
            print(sopt.text)
            assert sopt.is_displayed()

         
         


    

    
        



       
        

