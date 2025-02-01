import time
import pytest
from selenium.webdriver.common.by import By

# Тестовая функция
def test_guest_should_see_add_to_basket_button(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Добавляем паузу для визуальной проверки (требование задания)
    time.sleep(30)

    # Проверяем наличие кнопки "Добавить в корзину"
    try:
        add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert add_to_basket_button.is_displayed(), "Кнопка 'Добавить в корзину' не найдена!"
    except Exception as e:
        pytest.fail(f"Кнопка 'Добавить в корзину' отсутствует! {e}")