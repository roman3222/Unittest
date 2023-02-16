import requests
import json

class Yandex():
    def __init__(self, token):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'


    def get_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        return headers


    def create_folder(self, path):
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        res = requests.put(f'{self.url}?path={path}', headers=self.get_headers())
        return res


    def get_info(self, path):
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        res = requests.get(f'{self.url}?path={path}', headers=self.get_headers())
        return res



if __name__ == '__main__':
    ya = Yandex(token)
    print(ya.get_info('Homework_16').status_code)

