# class SingletonType(type):
#     def __init__(self, *args, **kwargs):
#         super(SingletonType, self).__init__(*args, **kwargs)

#     def __call__(cls, *args, **kwargs):
#         obj = cls.__new__(cls, *args, **kwargs)
#         cls.__init__(obj, *args, **kwargs)
#         return obj


class SingletonMeta(type):

    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            obj = cls.__new__(cls, *args, **kwargs)
            cls.__init__(obj, *args, **kwargs)
            cls.__instance = obj
            return cls.__instance
        else:
            return cls.__instance
