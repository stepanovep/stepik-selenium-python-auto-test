import time
from selenium import webdriver
import math


def calc(x):
    return str(math.log(math.fabs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)

    browser.find_element_by_css_selector('button.trollface').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)

    input_element = browser.find_element_by_id('answer')
    input_element.send_keys(str(calc(x)))

    submit_btn = browser.find_element_by_css_selector('button.btn')
    submit_btn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
