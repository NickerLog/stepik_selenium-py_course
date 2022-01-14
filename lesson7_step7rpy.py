from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element_by_id('treasure')
    x = x_elem.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element_by_css_selector('input[id="answer"]')
    input1.send_keys(y)

    checkbox_robot = browser.find_element_by_css_selector('input[id="robotCheckbox"]')
    checkbox_robot.click()

    radio_robots = browser.find_element_by_css_selector('input[id="robotsRule"]')
    radio_robots.click()

    button_submit = browser.find_element_by_css_selector('button[type="submit"]')
    button_submit.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
