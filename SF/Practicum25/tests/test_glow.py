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
    pytest.driver.implicitly_wait(5)
    pytest.driver.get('http://glowworm59.ucoz.net/index/my_pets/0-9')

    yield

    pytest.driver.quit()


def test_my_pets():
    # проверяем имя таблицы
    # name_table = pytest.driver.find_element(by=By.TAG_NAME, value='strong')
    # name_table = pytest.driver.find_element_by_tag_name('strong').text
    # pytest.driver.implicitly_wait(5)
    name_table = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, 'strong')))
    name_table = name_table.text
    print('name_table=')
    print(type(name_table))
    print(name_table)
    assert name_table == "Мои питомцы", 'Ничего не найдено'

    # находим количество строк в таблице с питомцами
    # так тоже можно count_table = pytest.driver.find_element(
    #    by=By.XPATH, value='//*[@id="contanier"]/table[2]/tbody[1]/tr[1]/td[2]/div[1]')
    # count_table = pytest.driver.find_element(
    #    by=By.CSS_SELECTOR, value='div#contanier > table:nth-of-type(2) > tbody > tr > td:nth-of-type(2) > div')
    # pytest.driver.implicitly_wait(5)
    count_table = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, 'div#contanier > table:nth-of-type(2) > tbody > tr > td:nth-of-type(2) > div')))
    count_table = count_table.text
    count_table = count_table.split()
    count_table = int(count_table[1])
    print('count_table =', count_table)
    assert count_table > 0, 'Нет данных Статистика:'

    # Находим количество питомцев с фотографиями
    images = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'IMG')))
    print('len(images) =')
    print(len(images))
    # print(type(images))
    # print(images)
    assert len(images) >= count_table // 2 + 1, 'Недостаточно питомцев с фотографиями'

    photo_presence = 0
    pytest.driver.implicitly_wait(5)
    # Через проверку у всех питомцев, что attribute 'src' не пустое значение, определяем
    # количество питомцев с фотографией
    for i in range(count_table):
        if images[i].get_attribute('src') != '':
            photo_presence += 1
    # Проверяем, что как min половина всех питомцев имеет фотографию
    assert photo_presence >= (count_table // 2),'Недостаточно питомцев с фотографиями'

    # Проверяем, что в списке нет повторяющихся питомцев и
    # у питомцев заполнены все данные: имя, тип, возраст
    # Формируем массив.
    myList = []
    # постоянная часть в Xpath
    cXpath = '//table[2]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr['
    for i in range(1, count_table + 1):
        stroka = ''
        pytest.driver.implicitly_wait(5)
        name = pytest.driver.find_element_by_xpath(cXpath + str(i) + "]/td[2]/span[1]").text
        assert name != '', 'У питомца отсутствует имя'
        stroka += name
        tip = pytest.driver.find_element_by_xpath(cXpath + str(i) + "]/td[3]/span[1]").text
        assert tip != '', 'У питомца отсутствует тип'
        stroka += tip
        age = pytest.driver.find_element_by_xpath(cXpath + str(i) + "]/td[4]/span[1]").text
        assert age != '', 'У питомца отсутствует возраст'
        stroka += age
        myList.append(stroka)
    print(myList)
    assert myList != [], 'Массив пустой'
    # для проверки на совпадение строк массива сформируем массив из уникальных строк.
    # Если длина массива осталась прежней, значит нет повторяющихся строк.
    mySet = set(myList)
    print('mySet=', mySet)
    print(len(mySet))
    assert len(mySet) == count_table, 'В списке есть повторяющиеся питомцы'


#  для запуска в Терминале меняем окружение cd F:\__QAP\Pycharm\modul25\tests
#  python -m pytest -v  test_glow.py  прописываем в терминал для запуска, путь к драйверу уже прописан в фикстуре
