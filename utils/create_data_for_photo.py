import json


def gen_data_for_photo(photos):
    for k, v in photos.items():
        size = v['size']
        file_data = ({"file_name": f"{k}.jpg", "size": f"{size}"})
        with open(f'output/{k}.json', 'w') as f:
            json.dump(file_data, f, indent=2)
