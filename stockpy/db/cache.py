import os
import simplejson as json


class Cache:

    def __init__(self, **opts):
        self.__data_path = opts['data_path']

    def get(self, type: str):
        try:
            with open(self.__file_path(type), 'r') as f:
                s = f.read()
                if s == None:
                    return s
                return json.loads(s)
        except FileNotFoundError:
            return None

    def save(self, type: str, data):
        file_path = self.__file_path(type)

        def do_save():
            with open(file_path, 'w+') as f:
                jd = json.dumps(data, ensure_ascii=False,
                                encoding="utf-8", indent=4 * ' ')
                return f.write(jd)

        try:
            do_save()
        except FileNotFoundError:
            os.makedirs(os.path.dirname(file_path))
            do_save()

    def __file_path(self, type: str):
        return '{}/{}'.format(self.__data_path, type)
