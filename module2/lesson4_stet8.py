from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import pyperclip


def calc(x):
    return str(math.log(math.fabs(12 * math.sin(x))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '$100')
)

book_button = browser.find_element_by_id('book')
book_button.click()

x_element = browser.find_element_by_id('input_value')
x_element.get_attribute()
x = int(x_element.text)
answer = str(calc(x))

input_element = browser.find_element_by_id('answer')
input_element.send_keys(answer)

submit_button = browser.find_element_by_id('solve')
submit_button.click()

# Копирование числа из алерта в буфер обмена
alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)

