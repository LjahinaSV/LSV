import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    # pytest.driver = webdriver.Chrome('./chromedriver.exe')
    # (executable_path=r 'F:\__QAP\Pycharm\modul25\chromedriver.exe')
    pytest.driver = webdriver.Chrome(executable_path=r'F:\__QAP\Pycharm\modul25\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def test_all_pets():
    # Авторизация на сайте.
    # Вводим email
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element_by_id('email').send_keys('Frosya@test.test')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('123123')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

    pytest.driver.implicitly_wait(10)
    # pytest.driver.get('http://petfriends1.herokuapp.com/login')
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_my_pets():
    # Авторизация на сайте.
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('Frosya@test.test')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('123123')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Заходим на страницу своих питомцев
    pytest.driver.find_element_by_css_selector("div#navbarNav > ul > li > a").click()

    assert pytest.driver.find_element_by_tag_name('h2').text == "Frosya"

    # ====== ??? дальше я не проверила  ???
    # Проверяем, что на странице со списком моих питомцев, хотя бы у половины питомцев есть фото
    # element = WebDriverWait(pytest.driver, 10).
    # until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    # Сохраняем в переменную ststistic элементы статистики
    # statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")
    statistic = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    # Сохраняем в переменную images элементы с атрибутом img
    images = pytest.driver.find_elements_by_css_selector('.table.table-hover img')

    # Получаем количество питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    # rows = pytest.driver.find_element_by_css_selector('.table, table-hover tr')
    rows = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table, table-hover tr")))

    assert number == len(rows) - 1

    # Выбираем моих питомцев локатором кнопки удаления животного
    del_pet = pytest.driver.find_elements_by_xpath('//td[@class="smart_cell"]')
    pytest.driver.implicitly_wait(5)
    # Выбираем все элементы фотографий питомцев пользователя
    images = pytest.driver.find_elements_by_xpath('//th/img')
    pytest.driver.implicitly_wait(5)

    # Назначаем переменную для подсчёта количества питомцев пользователя с фотографией
    photo_presence = 0
    pytest.driver.implicitly_wait(5)
    # Через проверку у всех питомцев, что attribute 'src' не пустое значение, определяем
    # количество питомцев с фотографией
    for i in range(len(del_pet)):
        if images[i].get_attribute('src') != '':
            photo_presence += 1
        else:
            photo_presence = photo_presence
    # Проверяем, что как min половина всех питомцев имеет фотографию
    assert photo_presence >= (len(del_pet) / 2)

    # проверка уникальности имен
    # сохраняем все имена в массив
    names = pytest.driver.find_elements_by_xpath('//tbody/tr/td[1]')
    # names = WebDriverWait(pytest.driver, 10).until(
    #    EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[1]")))
    pytest.driver.implicitly_wait(5)
    for i in range(len(names) - 1):
        nam1 = names[i].text
        for j in range(len(names) - 1):
            nam2 = names[j].text
            if i != j:
                assert nam1 != nam2, 'Есть совпадающие имена'

    # У всех питомцев есть имя, возраст и порода.
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element_by_xpath(
        '//*[@id="all_my_pets"]/table/tbody/tr[1]' and
        '//*[@id="all_my_pets"]/table/tbody/tr[2]' and
        '//*[@id="all_my_pets"]/table/tbody/tr[3]').text != ''

    # У всех питомцев разные имена, породы и возраст.
    pytest.driver.implicitly_wait(5)
    name_type_age1 = pytest.driver.find_element_by_xpath(
        '//*[@id="all_my_pets"]/table/tbody/tr[1]/td[1]' and
        '//*[@id="all_my_pets"]/table/tbody/tr[1]/td[2]' and
        '//*[@id="all_my_pets"]/table/tbody/tr[1]/td[3]')
    name_type_age2 = pytest.driver.find_element_by_xpath(
        '//*[@id="all_my_pets"]/table/tbody/tr[2]/td[1]' and
        '//*[@id="all_my_pets"]/table/tbody/tr[2]/td[2]' and
        '//*[@id="all_my_pets"]/table/tbody/tr[2]/td[3]')
    name_type_age3 = pytest.driver.find_element_by_xpath(
        '//*[@id="all_my_pets"]/table/tbody/tr[3]/td[1]' and
        '//*[@id="all_my_pets"]/table/tbody/tr[3]/td[2]' and
        '//*[@id="all_my_pets"]/table/tbody/tr[3]/td[3]')
    assert name_type_age1 != name_type_age2 != name_type_age3

#  для запуска в Терминале меняем окружение cd F:\__QAP\Pycharm\modul25\tests
#  python -m pytest -v  test_pets.py  прописываем в терминал для запуска, путь к драйверу уже прописан в фикстуре
