class Person:
    counter = 0
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        Person.counter += 1
    
    def showInfo(self):
        print(f'Name: ', self.name)
        print(f'Gender: ', self.gender)
    
    @classmethod
    def showCount(_):
        print('Number of objeobject created', _.counter)

nibu = Person('Nibu', 'M')
bat = Person('Bat', 'M')
Person.showCount()