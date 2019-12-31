
import time
import threading
import asyncio
import math


class RateLimiter:

    def __init__(self, rate: int, capacity: int):
        '''
        Args:
            rate:   the velocity of the token generation
            capacity: total count of tokens
        '''
        self._lock = threading.Lock()
        self._rate = rate
        self._capacity = capacity
        self._size = 0
        self._last_request_time = int(time.time())

    def acquire(self, count) -> bool:
        '''
        Args:
            count: the count of token aqcuired
        '''
        with self._lock:
            inc = (time.time() - self._last_request_time) * self._rate
            self._size = min(inc + self._size, self._capacity)            
            if count > self._size:
                return False
            self._last_request_time = int(time.time())
            self._size -= count
            return True


class RateQueue(list):

    def __init__(self, rate: int, capacity: int):
        self.__bucket = RateLimiter(rate, capacity)
        self.__items = []

    async def append(self, item):
        while True:
            if self.__bucket.acquire(1) is True:
                self.__items.append(item)
                return
            else:
                print('sleep 1s')
                await asyncio.sleep(1)
