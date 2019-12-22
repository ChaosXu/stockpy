import requests
import simplejson as json


class Client:

    def __init__(self, **config):
        self.__http_url = config['http_url']
        self.__token = config['token']
        self.__timeout = config['timeout']

    def query(self, api_name, fields='', **kwargs):
        req_params = {
            'api_name': api_name,
            'token': self.__token,
            'params': kwargs,
            'fields': fields
        }

        res = requests.post(self.__http_url, json=req_params,
                            timeout=self.__timeout)
        result = json.loads(res.text)
        if result['code'] != 0:
            raise Exception(result['msg'])
        data = result['data']
        # columns = data['fields']
        # items = data['items']
        return data
        
