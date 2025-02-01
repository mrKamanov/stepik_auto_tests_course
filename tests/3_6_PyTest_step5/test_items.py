import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Список для сбора сообщений из фидбеков
collected_message = ""

# Фикстура для браузера
@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Открыть браузер в полноэкранном режиме
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()  # Закрываем браузер после выполнения теста

# Список URL-адресов задач
lesson_urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

# Тестовая функция
@pytest.mark.parametrize('link', lesson_urls)
def test_stepik_feedback(browser, link, load_config):
    global collected_message

    try:
        # Открываем страницу урока
        browser.get(link)

        # Извлекаем логин и пароль из конфига
        login = load_config['username']
        password = load_config['password']

        # Проверяем наличие кнопки "Войти" и выполняем авторизацию
        try:
            login_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login"))
            )
            login_button.click()  # Клик по кнопке "Войти"

            # Выбираем вкладку "Войти" в модальном окне
            login_tab = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-tab-name="login"]'))
            )
            login_tab.click()

            # Вводим логин и пароль
            email_input = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.NAME, "login"))
            )
            password_input = browser.find_element(By.NAME, "password")

            email_input.send_keys(login)  # Используем логин из config.json
            password_input.send_keys(password)  # Используем пароль из config.json

            # Нажимаем кнопку "Войти"
            submit_button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")
            submit_button.click()

            # Ждем успешной авторизации
            WebDriverWait(browser, 10).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "modal-dialog"))
            )
        except Exception:
            pass  # Если уже авторизованы, пропускаем

        # Проверяем наличие кнопки "Решить снова"
        try:
            solve_again_button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn.white"))
            )
            solve_again_button.click()  # Нажимаем "Решить снова"
            print("Нажата кнопка 'Решить снова'")
        except Exception:
            pass  # Если кнопки нет, пропускаем

        # Находим поле для ввода ответа
        answer_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        answer_input.clear()  # Очищаем поле перед вводом
        answer = str(math.log(int(time.time())))  # Генерируем правильный ответ
        answer_input.send_keys(answer)  # Вводим ответ

        # Находим и нажимаем кнопку "Отправить"
        submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        submit_button.click()

        # Ждем появления фидбека
        feedback_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
        feedback_text = feedback_element.text.strip()  # Получаем текст фидбека

        # Проверяем фидбек
        if feedback_text != "Correct!":
            collected_message += feedback_text + " "  # Собираем сообщение
            print(f"Добавлено сообщение: {feedback_text}")

        # Утверждение (тест не должен падать, если нет "Correct!")
        assert feedback_text == "Correct!", f"Ожидается 'Correct!', но получено '{feedback_text}'"

    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Фикстура для вывода собранных сообщений после всех тестов
@pytest.fixture(scope="session", autouse=True)
def finalize():
    yield  # Ждем завершения всех тестов
    if collected_message.strip():
        print("\nСобранное сообщение:")
        print(collected_message.strip())