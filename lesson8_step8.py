from selenium import webdriver
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_form = browser.find_element_by_name('firstname')
    first_name_form.send_keys('Ivan')

    last_name_form = browser.find_element_by_name('lastname')
    last_name_form.send_keys('Ivanov')

    email_form = browser.find_element_by_name('email')
    email_form.send_keys('Ivanov23@mail.com')

    attach_file = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'bio.txt')
    attach_file.send_keys(file_path)

    print("directory: ", current_dir, "full filepath: ", file_path)

    button_submit = browser.find_element_by_css_selector('button[type="submit"]')
    button_submit.click()




finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
