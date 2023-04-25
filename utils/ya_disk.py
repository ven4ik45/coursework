import requests


class Uploader:
    def __init__(self, ya_token: str):
        self.ya_token = ya_token

    def get_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.ya_token}'
        }
        return headers

    def get_upload_url(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {
            'path': path_to_file,
            'overwrite': 'true'
        }
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def create_catalog(self, catalog):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        params = {
            'path': catalog,
            'overwrite': 'true'
        }
        response = requests.get(url=upload_url, headers=headers, params=params)
        if response.status_code == 404:
            requests.put(url=upload_url, headers=headers, params=params)

    def upload(self, photo_url, catalog: str, file_name: str):
        path_to_file = f'{catalog}/{file_name}'
        headers = self.get_headers()
        pr = photo_url
        params = {
            'path': f'{path_to_file}.jpg',
            'url': pr
        }
        self.create_catalog(catalog)
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        requests.post(url=upload_url, headers=headers, params=params)
        json_data = self.get_upload_url(f'{path_to_file}.json')
        link_to_upload = json_data['href']
        requests.put(link_to_upload, data=open(f'output/{file_name}.json', 'r'))
