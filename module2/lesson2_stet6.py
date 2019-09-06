import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(math.fabs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = int(browser.find_element_by_id("input_value").text)
    answer = calc(x)

    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(answer)
    time.sleep(0.5)

    submit_button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(0.5)

    checkbox_buttons_ids = ['robotCheckbox', 'robotsRule']
    for button_id in checkbox_buttons_ids:
        browser.find_element_by_id(button_id).click()

    time.sleep(0.5)
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
