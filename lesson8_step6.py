from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elem_x = browser.find_element_by_id('input_value')
    x = int(elem_x.text)
    answer = calc(x)

    answer_field = browser.find_element_by_id('answer')
    browser.execute_script('return arguments[0].scrollIntoView(true);', answer_field)
    answer_field.send_keys(answer)

    checkbox_click = browser.find_element_by_id('robotCheckbox')
    browser.execute_script('return arguments[0].scrollIntoView(true);', checkbox_click)
    checkbox_click.click()

    radio_click = browser.find_element_by_id('robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', radio_click)
    radio_click.click()

    button_submit = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button_submit)
    button_submit.click()



finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
