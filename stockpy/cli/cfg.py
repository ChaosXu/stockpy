import simplejson as json


def load_cfg(path: str):
    with open(path, 'r') as f:
        s = f.read()
        if s is None:
            return s
        return json.loads(s)
