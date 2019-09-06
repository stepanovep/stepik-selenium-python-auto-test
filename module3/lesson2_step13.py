from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):

    def test_abs1(self):
        self.execute("http://suninjuly.github.io/registration1.html")

    def test_abs2(self):
        self.execute("http://suninjuly.github.io/registration2.html")

    @staticmethod
    def execute(link):
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_block = browser.find_element_by_class_name("first_block")

        first_name_input = first_block.find_element_by_css_selector(".first_class > input")
        first_name_input.send_keys("FirstName")

        last_name_input = first_block.find_element_by_css_selector(".second_class > input")
        last_name_input.send_keys("LastName")

        email_input = first_block.find_element_by_css_selector(".third_class > input")
        email_input.send_keys("email@gmail.com")

        second_block = browser.find_element_by_class_name("second_block")

        phone_input = second_block.find_element_by_css_selector(".first_class > input")
        phone_input.send_keys("8911900123123")

        address_input = second_block.find_element_by_css_selector(".second_class > input")
        address_input.send_keys("Saint-Petersburg")

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


if __name__ == "__main__":
    unittest.main()
