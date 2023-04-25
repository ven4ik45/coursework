from utils import ya_disk as ya
from utils import vk as vk
from utils import token as t
from utils import create_data_for_photo as dp
import os


ya_token = t.get_creds('ya')
vk_token = t.get_creds('vk')
vk_user_id = t.get_creds('vk_user_id')

vk = vk.VK(vk_token, vk_user_id)
ya = ya.Uploader(ya_token)

owner_id = '3113239'
album = 'profile'
count = '5'
catalog = f'id_vk_{owner_id}'

photos = vk.get_user_photos(owner_id, album, count)
dp.gen_data_for_photo(photos)

for i in photos.values():
    url = i['url']
    file = i['file_name']
    ya.upload(url, catalog, file)


path = 'output/'
for f in os.listdir(path):
    os.remove(os.path.join(path, f))
