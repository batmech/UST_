from optparse import Values


name = 'Bat'
number = 12
items = ['apples', 'mangoes']
transaction = ('Bat', 123345)
Bale = {
    'Super-Hero' : 'Batman',
    'age' : 49,
    'bacholeor' : 'Da'  
}

class Graph:
    def __init__(self):
        self.graph = {}
        
    def addVertex(self, vertex):
        if vertex not in self.graph: self.graph[vertex] = []
    
    def addEdge(self, first, sec):
        if first in self.graph and sec in self.graph:
            self.graph[first].append(sec)
            
    def display(self):
        for item in self.graph:
            print(f'{item} -> {self.graph[item]}')

tester = Graph()
tester.addVertex('A')
tester.addVertex('B')
tester.addVertex('C')
tester.addVertex('D')
tester.addEdge('A', 'B')
tester.addEdge('A', 'C')
tester.addEdge('A', 'D')
tester.addEdge('B', 'C')
tester.addEdge('B', 'D')
tester.addEdge('C', 'D')
tester.addEdge('D', 'B')
tester.addEdge('D', 'C')
tester.addEdge('D', 'A')
tester.display()


keys = tuple(input('Enter key elements: ').split())
value = tuple(input('Enter value elements: ').split())

dictValues = {key:value for key,value in zip(keys, value)}
print(dictValues)

age = 22
print('Hello this is {}'.format('Allwyn'))
print(f'I am {age} years old')
print('I am', 'looking into chess')
print('Hello this is a greetiing from %s'%('ABOVE!!'))
print('12' + ' + ' + '12' + ' != ' + '12' + '12')


string = 'india'
first = string.find('i')
sec = string[first+1:].find('i')
print(sec)

lt = [1, [1, 2, [1, 0, 2, [0, 1, 2, 3, 4, 5], 4, 5, ], 5], 43, 5, 6, 7]
print(lt[1][2][3][4])


# Removing the second occurance of Java
items = ['Java', 'C++', 'Java', 'Python']
ind = items.index('Java')
items = [val for i,val in enumerate(items) if val != 'Java' or i == ind]
print(items)

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
        print('Try again!!')

from Day2.__Day2__ import validData

validData()