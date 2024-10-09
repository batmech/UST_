from audioop import add
from unicodedata import name


class Distance:
    def __init__(self, meter, cm) -> None:
        self.meter = meter
        self.cm = cm
    
    def __str__(self):
        return f'Distance: {self.meter} meters {self.cm} cms '
    
    def __add__(self, other):
        if isinstance(other, Distance):
            val = self.meter + other.meter
            cms = self.cm + other.cm
            while cms >= 100:
                val += 1
                cms -= 100
            return Distance(val, cms)



# first = Distance(1, 140)
# sec = Distance(3, 90)
# third = first + sec
# print(third)
# print(dir(int))


class Operator:
    def __init__(self, item1):
        self.item = item1
        
    def __str__(self):
        return f'Result in Object: {self.item}'
    
    def __and__(self, other):
        if isinstance(other, Operator):
            return Operator(self.item & other.item)
    
    def __or__(self, other):
        if isinstance(other, Operator):
            return Operator(self.item | other.item)
    
    def __add__(self, other):
        if isinstance(other, Operator):
            val = self.item + other.item
            return Operator(val)
        
    def __sub__(self, other):
        if isinstance(other, Operator):
            val = self.item - other.item
            return Operator(val)
        
    def __mul__(self, other):
        if isinstance(other, Operator):
            val = self.item * other.item
            return Operator(val)


first = Operator(3)
sec = Operator(4)
andAns = first & sec
orAns = first | sec
addAns = first + sec
subAns = first - sec
mul = first * sec

print(andAns)
print(orAns)
print(addAns)
print(subAns)
print(mul)