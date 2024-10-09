import time
from functools import lru_cache

@lru_cache(maxsize=100)
def func(s):
    if s <= 1: return s
    return func(s-1) + func(s-2)

if __name__ == '__main__':
    print('Result:', func(400))
    print('Result:', func(19))
    print('Result:', func(28))
    print('Result:', func(12))
    


# from functools import lru_cache
# import requests
# from random import choice


# @lru_cache(maxsize = 1)
# def get_data():
#     data = requests.get("http://jsonplaceholder.typicode.com/photos").json()
#     return data


# def receiver():
#     while True:
#         x = yield
#         print("Recieved:", x)


# channel = receiver()
# next(channel)

# while True:
#     input("Press any key to fetch random title from API ")
#     channel.send(choice(get_data())['title'])
