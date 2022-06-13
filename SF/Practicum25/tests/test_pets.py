import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('chromedriver.exe')  # находится в папке tests
    # pytest.driver = webdriver.Chrome(executable_path=r'F:\__QAP\Pycharm\modul25\tests\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.implicitly_wait(5)
    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_all_pets():
    # Авторизация на сайте.
    # Вводим email
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.ID, 'email').send_keys('Frosya@test.test')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('123123')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        print('i =', i, 'names[i].text =', names[i].text)
        assert images[i].get_attribute('src') != '', "Нет фото"
        assert names[i].text != '', "Нет имени"
        assert descriptions[i].text != '', "Поле порода и возраст - пустое"
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(",")
        assert len(parts[0]) > 0, "Нет названия породы"
        assert len(parts[1]) > 0, "Нет возраста"

#  для запуска в Терминале меняем окружение на cd F:\__QAP\Pycharm\modul25\tests
#  прописываем в терминал для запуска строку
#  python -m pytest -v  test_pets.py
#  путь к драйверу уже прописан в фикстуре
