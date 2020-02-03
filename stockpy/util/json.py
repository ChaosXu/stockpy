import os
import json


def load_json(path: str):
    with open(path, 'r') as f:
        s = f.read()
        if s is None:
            return s
        return json.loads(s)


def save_json(path: str, data):
    def do_save(path: str, data):
        with open(path, 'w', encoding='utf-8',) as f:
            data_json = json.dumps(data, ensure_ascii=False)
            f.write(data_json)

    try:
        do_save(path, data)
    except FileNotFoundError:
        os.makedirs(os.path.dirname(path))
        do_save(path, data)
