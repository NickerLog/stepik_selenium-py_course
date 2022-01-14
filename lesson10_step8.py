from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5[id="price"]'), '$100'))
    button_book = browser.find_element_by_css_selector('button[id="book"]')
    button_book.click()

    x = int(browser.find_element_by_id('input_value').text)
    answer = calc(x)
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer)
    
    button_submit = browser.find_element_by_css_selector('button[type="submit"]')
    button_submit.click()


    print("you code is here: ", browser.switch_to.alert.text) #парсинг текста из алерта


finally:
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
