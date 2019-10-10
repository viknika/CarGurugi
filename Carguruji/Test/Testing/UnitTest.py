import unittest
from selenium import webdriver
from Selenium.Test.Pages.Logout import LogoutPage
from Selenium.Test.Pages.AddToCart import addtocartPage
from Selenium.Test.Pages.Login import LoginPage
from Selenium.Test.Pages.CheckOut import checkOutPage



class WAPTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/Veronika/PycharmProjects/Selenium/Test/Driver/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test2(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/login?back=my-account#account-creation")

        login = LoginPage(driver)
        login.SignIn("vikmor@gmail.com", "Vik159")

        driver.save_screenshot("D:/Veronika/PycharmProjects/Selenium/Test/Screen/login.png")

    def test3(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/my-account")

        add = addtocartPage(driver)
        add.search_item("dress")
        add.choose_item()
        add.add_item_to_cart()
        add.check_out()

        driver.save_screenshot("D:/Veronika/PycharmProjects/Selenium/Test/Screen/additem.png")

    def test4(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/order")

        checkout = checkOutPage(driver)
        checkout.proceed_check_out()
        checkout.enter_firstname("Vik")
        checkout.enter_bill_lastname("Mor")

        checkout.enter_bill_street("15 Tom Cook")
        checkout.enter_bill_city("Alabama")
        checkout.select_bill_state("Alabama")
        checkout.enter_bill_postcode("35005")
        checkout.select_bill_country("United States")
        checkout.enter_bill_phone("4168425789")
        checkout.save()
        checkout.cont_check_out()
        checkout.choose_payment()
        checkout.confirm()

        driver.save_screenshot("D:/Veronika/PycharmProjects/Selenium/Test/Screen/confirmation.png")




    def test5(self):
        driver = self.driver
        logout = LogoutPage(driver)
        logout.SignOut()

        driver.save_screenshot("D:/Veronika/PycharmProjects/Selenium/Test/Screen/logout.png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

