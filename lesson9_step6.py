from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_submit1 = browser.find_element_by_css_selector('button[type="submit"]')
    button_submit1.click()

    window1 = browser.window_handles[1]
    browser.switch_to.window(window1)

    elem_x = browser.find_element_by_id('input_value')
    x = int(elem_x.text)
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

