import requests
import simplejson as json
import pandas as pd
import time
from stockpy.util.rate import RateLimiter
from stockpy.db.driver import Driver


class Client(Driver):

    def __init__(self, **config):
        self.__http_url = config['http_url']
        self.__token = config['token']
        self.__timeout = config['timeout']
        self.__buckets = RateLimiter(config['rate'], config['capacity'])

    def query(self, api_name, fields='', **kwargs):
        req_params = {
            'api_name': api_name,
            'token': self.__token,
            'params': kwargs,
            'fields': fields
        }

        while self.__buckets.acquire(1) is False:
            time.sleep(1)

        res = requests.post(self.__http_url, json=req_params,
                            timeout=self.__timeout)
        result = json.loads(res.text)
        if result['code'] != 0:
            raise Exception(result['msg'])
        data = result['data']
        print('query', api_name, kwargs['ts_code'], kwargs['period'])
        return pd.DataFrame(data['items'], columns=data['fields'])
