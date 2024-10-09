# Immuntable Sets
from ast import iter_child_nodes
from tabnanny import check


values = {4, 1, 4, 6, 2, 3}
values.add(90)
values = frozenset(values)

# Deep Copy
lst = [1, 2, 3, 4, 5]
tester = lst
lst.append(6)

#Shallow Copy
tester = lst.copy()
lst.append(7)

# Math Table

num = int(input('Enter a number: '))
print(f"{num}'s Table")
for i in range(1, 16): print(f"{num} * {i} = {i*num}")

# Password Management

symbols = '#!@$%^&*()_+=-}{]['
smalls = 'abcdefghijklmnopqrstuvwxyz'
nums = '1234567980'
while True:
    password = input('Enter a password:')
    checkList = [False] * 3
    if len(password) < 8: print('Password should have atleast 8 characters')
    for char in password:
        if char.lower() in smalls: checkList[0] = True
        elif char in nums: checkList[1] = True
        elif char in symbols: checkList[2] = True
    
    if all(checkList):
        print('Password set successfully!!')
        break
    else:
        print('Try again')


import random 

flag =True
while flag:
    num = random.randint(1,6)
    print('Your number is :', num)
    if num < 6:
        flag = False
    else:
        pass
        print('Your turn again!')

print('Next persons turn')


import json

with open('output.txt', 'w') as fp:
    items = ['Java', 'Python']
    json.dump(items, fp)

with open('output.txt', 'r') as fp:
    items = json.load(fp)
    print(items[0], items[1])


def add(first, sec):
    print(globals()['num1'])
    print(f'Sum: {first+sec}')

def total(first, sec):
    return first + sec

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))

add(num1, num2)
print(total(num1, num2))

lst = ['Java', 'Python', 'C++', 'C', 'GoLang', 'PHP', 'CSS', 'HTML']
for ind, val in enumerate(lst, 5): #(5, 'Golang)
    print(ind, '->', val)


key = [i for i in range(1, 11)]
value = {i*2 for i in key}
dictValue = {key:val for key, val in zip(key, value)}

print(key)
print(value)
print(dictValue)

import random

def taker(*args, **kwargs):
    print(args)
    print(kwargs)

names = [i for i in input('Enter names: ').split(',')]
ages = [random.randint(18,35) for _ in names]
persons = {key:val for key, val in zip(names, ages)}
taker(*names, **persons)

import re

def validData():
    phonePatter = r'\+?\d{2,3} ?\d{5} ?-?\d{5}'
    emailPatter = r'[a-z.]+@\S+\.[com|gov|in]+'
    with open('input.txt', 'r') as fp:
        data = fp.read()
        emails = re.findall(emailPatter, data)
        mobile = re.findall(phonePatter, data)
        print('Numbers:', mobile)
        print('Emails:', emails)


validData()

import time

num = 10_000_000
def tester(num): return list(map(str, range(num)))

start = time.time()
check = lambda num:  [str(i) for i in range(num)]
end = time.time()
print('Lamda and List Comprehension: ', end - start)

start = time.time()
value = tester(num)
end = time.time()
print('Function call: ', end-start)

import unittest
import tester

class Testing(unittest.TestCase):
    def testNumberOne(self):
        test = 4
        result = tester.calc_num(test, test)
        self.assertEqual(result, 8)
        
    def testNumberTwo(self):
        num1 = 4
        num2 = 5
        result = tester.calc_num(num1, num2)
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()