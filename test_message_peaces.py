from selenium import webdriver
import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1', 'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1', 'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1', 'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
class TestMessagePeaces:
    def test_mess_peaces_collecting(self, browser, link):
        browser.implicitly_wait(10)
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, 'textarea')
        input1.send_keys(str(math.log(int(time.time()))))
        button_send = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
        button_send.click()
        message = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'pre.smart-hints__hint'))).text
        assert message == 'Correct!', f'\nmessage is: {message}'







