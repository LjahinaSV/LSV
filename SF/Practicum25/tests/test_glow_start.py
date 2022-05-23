import pytest
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(executable_path=r'F:\__QAP\Pycharm\modul25\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.implicitly_wait(5)
    pytest.driver.get('http://glowworm59.ucoz.net/')

    yield

    pytest.driver.quit()


def test_ignition():
    pytest.driver.implicitly_wait(5)
    # assert pytest.driver.find_element_by_tag_name('h1').text == "Мой сайт-учебник"
    assert pytest.driver.find_element(by=By.TAG_NAME, value="h1").text == "Мой сайт-учебник"


#  для запуска в Терминале меняем окружение cd F:\__QAP\Pycharm\modul25\tests
#  python -m pytest -v  test_glow_start.py  прописываем в терминал для запуска, путь к драйверу уже прописан в фикстуре
