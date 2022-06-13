import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    # pytest.driver = webdriver.Chrome('chromedriver.exe')  # находится в папке tests
    pytest.driver = webdriver.Chrome(executable_path=r'F:\__QAP\Pycharm\modul25\tests\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.implicitly_wait(5)
    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_my_pets():
    wait = WebDriverWait(pytest.driver, 5)
    # Авторизация на сайте.
    # Вводим email
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys('Frosya@test.test')

    # Вводим пароль
    wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys('123123')

    # Нажимаем на кнопку входа в аккаунт
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))).click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Заходим на страницу своих питомцев
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#navbarNav > ul > li > a"))).click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "Frosya"
    # количество питомцев
    # сохраняем в переменную data_statistic элементы статистики
    data_statistic = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    # Получаем количество питомцев из данных статистики
    statistic = data_statistic[0].text.split('\n')
    statistic = statistic[1].split(' ')
    statistic = int(statistic[1])
    print('statistic= ', statistic)
    assert statistic > 0, "Нет данных Статистика"
    # Проверяем, что количество строк в таблице равно числу, записанному в статистике
    # count_table - количество строк таблицы определим по количеству элементов с атрибутом img
    images = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'IMG')))
    count_table = len(images) - 1
    print('count_table =', count_table)
    assert count_table >= 0, "Таблица 'Мои питомцы' - пустая"
    assert statistic == count_table, \
        'Данные Статистика не совпадают с количеством строк в таблице Мои питомцы'
    # Назначаем переменную для подсчёта количества питомцев пользователя с фотографией
    pytest.driver.implicitly_wait(5)
    photo_presence = 0
    # определяем количество питомцев с фотографией по непустому значению атрибута scr
    for i in range(count_table):
        photo = images[i].get_attribute('src')
        if photo != '' \
                and photo != 'https://petfriends.skillfactory.ru/static/images/upload2.jpg' and photo != '(unknown)':
            photo_presence += 1
        else:
            photo_presence = photo_presence
            # print('photo=', photo)
    print('photo_presence=', photo_presence, ' count_table // 2 =', count_table // 2)
    # Проверяем, что как минимум половина всех питомцев имеют фотографию
    assert photo_presence >= (count_table // 2), 'Недостаточно питомцев с фотографиями'

    # Проверяем, что у питомцев заполнены все данные: имя, тип, возраст
    # Формируем массив о всеми данными питомцев.
    myList = []
    # Формируем массив только с именами питомцев
    myNames = []
    # постоянная часть в Xpath
    cXpath = '//*[@id="all_my_pets"]/table/tbody/tr['
    for i in range(1, count_table + 1):
        stroka = ''
        pytest.driver.implicitly_wait(5)
        name = pytest.driver.find_element(By.XPATH, cXpath + str(i) + "]/td[1]").text
        assert name != '', 'У питомца отсутствует имя'
        stroka += name
        myNames.append(stroka)
        tip = pytest.driver.find_element(By.XPATH, cXpath + str(i) + "]/td[2]").text
        assert tip != '', 'У питомца отсутствует порода'
        stroka += tip
        age = pytest.driver.find_element(By.XPATH, cXpath + str(i) + "]/td[3]").text
        assert age != '', 'У питомца отсутствует возраст'
        stroka += age
        myList.append(stroka)
    print(myList)
    print(myNames)
    assert myList != [], 'Массив пустой'
    assert myNames != [], 'Массив имён пустой'
    # Проверяем, что в списке нет повторяющейся информации о питомцах (имя, порода, возраст)
    # Для этого сформируем новый массив из уникальных строк массива myList.
    # Если длина массива осталась прежней, значит нет повторяющихся строк.
    mySet = set(myList)
    print('mySet=', mySet, ' len(mySet)=', len(mySet))
    assert len(mySet) == count_table, 'В списке есть повторяющаяся информация о питомцах'

    # Проверяем, что в списке нет повторяющихся имён питомцев
    # Для этого сформируем новый массив из уникальных строк массива myNames.
    # Если длина массива осталась прежней, значит нет повторяющихся имён.
    mySet_Names = set(myNames)
    print('mySet_Names=', mySet_Names, ' len(mySet_Names)=', len(mySet_Names))
    assert len(mySet_Names) == count_table, 'В списке есть повторяющиеся имена питомцев'


#  для запуска в Терминале меняем окружение на cd F:\__QAP\Pycharm\modul25\tests
#  прописываем в терминал для запуска строку
#  python -m pytest -v  test_mypets.py
#  путь к драйверу уже прописан в фикстуре
