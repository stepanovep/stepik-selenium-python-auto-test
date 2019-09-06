from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    form_data = [
        dict(css_selector='.first_block input.first', value='Ivan'),
        dict(css_selector='.first_block input.second', value='Petrov'),
        dict(css_selector='.first_block input.third', value='test@email.com'),
        dict(css_selector='.second_block .first', value='+7-987-6543210'),
        dict(css_selector='.second_block .second', value='Address 123'),
    ]
    for data in form_data:
        input = browser.find_element_by_css_selector(data['css_selector'])
        input.send_keys(data['value'])

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
