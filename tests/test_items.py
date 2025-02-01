import time
from selenium.webdriver.common.by import By


def test_check_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Для визуальной проверки
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button is not None, "Button 'Add to cart' is not presented"