import json


def get_creds(name_service):
    with open('utils/creds.json') as f:
        token = json.load(f)[name_service]
        return token
