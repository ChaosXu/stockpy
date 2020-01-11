from stockpy.db import driver


class Driver(driver.Driver):

    def __init__(self, **opts):
        self.__data_path = opts['data_cache']['data_path']

    def query(self, api_name, fields='', **kwargs):
        raise Exception("could not found the data in the path {}, api={},period={}".format(
            self.__data_path, api_name, kwargs['period']))
