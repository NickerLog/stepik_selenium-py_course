from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el1 = browser.find_element_by_id('num1')
    el2 = browser.find_element_by_id('num2')

    num1 = int(el1.text)
    num2 = int(el2.text)
    summ = num1 + num2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summ))

    button_submit = browser.find_element_by_css_selector('button[type="submit"]')
    button_submit.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

