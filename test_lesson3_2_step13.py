from selenium import webdriver
import unittest
import time

class RegistrationTest(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        input1 = browser.find_element_by_css_selector(".form-control.first[required]")
        input1.send_keys("12")
        input1 = browser.find_element_by_css_selector(".form-control.second[required]")
        input1.send_keys("123")
        input1 = browser.find_element_by_css_selector(".form-control.third[required]")
        input1.send_keys("1234")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Failed Registration #1")
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        input1 = browser.find_element_by_css_selector(".form-control.first[required]")
        input1.send_keys("12")
        input1 = browser.find_element_by_css_selector(".form-control.second[required]")
        input1.send_keys("123")
        input1 = browser.find_element_by_css_selector(".form-control.third[required]")
        input1.send_keys("1234")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Failed Registration #2")


if __name__ == "__main__":
    unittest.main()





       
            

