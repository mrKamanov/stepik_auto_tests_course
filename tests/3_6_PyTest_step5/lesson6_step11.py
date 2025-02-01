# Тест регистрации на сайте с использованием Selenium.
# Скрипт проверяет корректность регистрации на двух страницах:
# 1. http://suninjuly.github.io/registration1.html - успешная регистрация.
# 2. http://suninjuly.github.io/registration2.html - проверка ошибки NoSuchElementException.
# Для выполнения теста необходимы: Selenium и ChromeDriver, соответствующий версии браузера Chrome.
# В ходе выполнения теста производится заполнение обязательных полей и отправка формы.
# При ошибке поиска элемента выводится сообщение об ошибке NoSuchElementException в консоль.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration_page(link):
    print(f"\n=== ТЕСТИРОВАНИЕ СТРАНИЦЫ {link} ===")
    try:
        browser = webdriver.Chrome()
        print(f"Открываем страницу: {link}")
        browser.get(link)

        # Ищем и заполняем поле First name
        try:
            print("Ищем поле First name и вводим данные...")
            input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
            input1.send_keys("Sergey")
            print("Поле First name заполнено.")
        except Exception:
            print("Ошибка: поле First name не найдено. Ошибка NoSuchElementException.")
            raise

        # Ищем и заполняем поле Last name
        try:
            print("Ищем поле Last name и вводим данные...")
            input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
            input2.send_keys("Kamanov")
            print("Поле Last name заполнено.")
        except Exception:
            print("Ошибка: поле Last name не найдено. Ошибка NoSuchElementException.")
            raise

        # Ищем и заполняем поле Email
        try:
            print("Ищем поле Email и вводим данные...")
            input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
            input3.send_keys("mr.k@")
            print("Поле Email заполнено.")
        except Exception:
            print("Ошибка: поле Email не найдено. Ошибка NoSuchElementException.")
            raise

        # Отправляем заполненную форму
        print("Отправляем форму...")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        print("Форма отправлена.")

        # Проверяем текст результата
        print("Ждём загрузки страницы...")
        time.sleep(1)
        print("Ищем элемент с текстом результата...")
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        print("Проверяем текст результата...")
        assert "Congratulations! You have successfully registered!" == welcome_text
        print(f"Тест на странице {link} пройден: регистрация прошла успешно!")

    except Exception as e:
        print(f"Ошибка на странице {link}: {str(e)}")
    except AssertionError:
        print(f"Ошибка: текст результата на странице {link} не совпадает с ожидаемым.")
    finally:
        print("Закрываем браузер через 5 секунд...")
        time.sleep(5)
        browser.quit()


# Тестируем первую страницу
test_registration_page("http://suninjuly.github.io/registration1.html")

# Тестируем вторую страницу
test_registration_page("http://suninjuly.github.io/registration2.html")
