
class Car:
    purpose = 'To move about efficiently!'
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def modelName(self):
        return f'Brand: {self.brand}'
    
    def __del__(self):
        print(f'Object => {self.brand} is destoryed!')
        
    def objectTst():
        print(f'{Car.purpose}')
        return 'End of Static method!'
    


bmw = Car('BMW M-6', 2016)
print(
    bmw.modelName()
)

del bmw
print(
    Car.objectTst()
)