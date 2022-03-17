import json

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """API библиотека к веб приложению Pet Friends"""

    # api_1
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    # api_2
    def get_api_key(self, email: str, passwd: str) -> json:
        """Метод делает запрос к API серверу
         и возвращает статус запроса и результат в формате JSON
         с уникальным ключом пользователя, найденным по указанным email и паролю"""

        headers = {
            'email': email,
            'password': passwd,
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    # api_3
    def get_list_of_pets(self, auth_key: json, filter: str = "") -> json:
        """Метод делает запрос к API серверу
         и возвращает статус запроса и результат в формате JSON
        со списком найденных питомцев, совпадающих с фильтром.
        На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев,
        либо 'my_pets' - получить список собственных питомцев"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    # api_4
    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        """Этот метод позволяет добавлять информацию о новом питомце
         и возвращает статус запроса на сервер и результат в формате JSON
          с данными добавленного питомца"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    # api_5
    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Этот метод позволяет удалить информацию о питомце из базы данных
         по указанному ID и возвращает статус запроса и результат в формате JSON
          с текстом уведомления об успешном удалении.
        На сегодняшний день тут есть баг - в result приходит пустая строка,
        но status при этом = 200"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    # api_6
    def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: int) -> json:
        """Этот метод позволяет обновлять информацию о питомце
         по указанному ID и возвращает статус запроса и результат в формате JSON
          с обновлёнными данными питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    # api_7
    def create_new_simple_pet(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        """Этот метод позволяет добавлять информацию о новом питомце без фото
         и возвращает статус запроса на сервер и результат в формате JSON
          с данными добавленного питомца"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/create_pets_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text

        return status, result

    # api_8
    def update_pet_photo(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Этот метод позволяет добавить фотографию питомца по указанному ID и
        возвращает статус запроса и результат в формате JSON с обновлёнными данными питомца"""

        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpg')
            })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
