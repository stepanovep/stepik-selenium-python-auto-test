import time
import os
from selenium import webdriver


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element_by_name('firstname').send_keys('FirstName')
    browser.find_element_by_name('lastname').send_keys('LastName')
    browser.find_element_by_name('email').send_keys('mail@mail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    file_attach_element = browser.find_element_by_id('file')
    file_attach_element.send_keys(file_path)

    submit_button = browser.find_element_by_css_selector('button.btn-primary')
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
