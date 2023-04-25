import requests


def get_params_photo(size_type, photo, name):
    params = {}
    for k in photo:
        if k['type'] == size_type:
            url = k['url']
            size = k['type']
            params = {'file_name': name, 'url': url, 'size': size}
    return params


def filter_photo_list(photos):
    photo_list = {}
    photo_type = ['w', 'z', 'y', 'r', 'q', 'p', 'o', 'x', 'm', 's']
    for k in photos['response']['items']:
        name = f"{k['likes']['count']}"
        sizes = []
        photo_params = {}
        for photo in k['sizes']:
            sizes.append(photo['type'])
        for i in photo_type:
            if i in sizes:
                photo_params = get_params_photo(i, k['sizes'], name)
                break
        photo_list[name] = photo_params
    return photo_list


class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def get_user_photos(self, owner_id, album, count=5):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': owner_id, 'album_id': album, 'count': count, 'extended': '1', 'photo_sizes': '1'}
        response = requests.get(url, params={**self.params, **params})
        photos = response.json()
        photo_list = filter_photo_list(photos)
        return photo_list
