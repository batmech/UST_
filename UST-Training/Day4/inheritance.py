class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age
        
    def typeOfAnimal(self):
        print(f'Animal => {self.species}, Age => {self.age}')

class Dog(Animal):
    def __init__(self, name, gender, species, age):
        Animal.__init__(self, species, age)
        self.name = name
        self.gender = gender

    def dogInfo(self):
        super().typeOfAnimal()
        print(f'Dog name => {self.name}\nDog gender => {self.gender}')


german = Dog('James', 'M', 'German Sherperd', 3)
german.dogInfo()