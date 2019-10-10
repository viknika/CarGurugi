from selenium import webdriver
from selenium.webdriver.support.ui import Select


class registerPage():

    def __init__(self,driver):
        self.driver = driver
        self.login_xpath = "/html[1]/body[1]/div[1]/div[1]/header[1]/div[2]/div[1]/div[1]/nav[1]/div[1]/a[1]"
        self.email_address_xpath = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]"
        self.create_account_xpath = "//form[@id='create-account_form']//span[1]"
        self.gender_female = "//input[@id='id_gender2']"
        self.gender_male = "//input[@id='id_gender1']"
        self.firstname_textbox_xpath = "//input[@id='customer_firstname']"
        self.lastname_textbox_xpath = "//input[@id='customer_lastname']"
        self.email_textbox_xpath = "//input[@id='email']"
        self.password_xpath = "//input[@id='passwd']"
        self.dob_year_xpath = "//select[@id='years']"
        self.dob_month_xpath = "//select[@id='months']"
        self.dob_day_xpath = "//select[@id='days']"
        self.register_button = "//span[contains(text(),'Register')]"



    def start_registr(self,email):
        self.driver.find_element_by_xpath(self.login_xpath).click()
        self.driver.find_element_by_xpath(self.email_address_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.create_account_xpath).click()

    def choose_gender(self,gender ):
        if gender =="Ms":
            self.driver.find_element_by_xpath(self.gender_male).click()
        if gender =="Mrs":
            self.driver.find_element_by_xpath(self.gender_female).click()


    def enter_firstname(self, firstname):
        self.driver.find_element_by_xpath(self.firstname_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.firstname_textbox_xpath).send_keys(firstname)
        #self.driver.implicity_wait(10)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_xpath(self.lastname_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.lastname_textbox_xpath).send_keys(lastname)
        #self.driver.implicity_wait(10)

    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email_textbox_xpath).clear()
        self.driver.implicity_wait(10)
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(email)



    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)


    def dateOfBirth(self, year,month,day):
        element_y = self.driver.find_element_by_xpath(self.dob_year_xpath)
        drp_y = Select(element_y)
        drp_y.select_by_visible_text(year)
        element_m = self.driver.find_element_by_xpath(self.dob_month_xpath)
        drp_m = Select(element_m)
        drp_m.select_by_visible_text(month)
        element_d = self.driver.find_element_by_xpath(self.dob_day_xpath)
        drp_d = Select(element_d)
        drp_d.select_by_visible_text(day)


    def regist(self):
        self.driver.find_element_by_xpath(self.register_button).click()



