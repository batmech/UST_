class A:
    def __init__(self, specs):
        self.specs = specs
        print(f'Class A initialized with {self.specs} specs')

class B:
    def __init__(self, value) -> None:
        self.value = value
        print(f'Class B initialized with {self.value} value')

class C(A, B):
    def __init__(self, specs, value):
        A.__init__(self, specs)
        B.__init__(self, value)
        print(f'Class C is initialized with {self.specs}, {self.value}')

class D(A):
    def __init__(self, specs, dValue):
        self.dValue = dValue
        super().__init__(specs)
        print(f'Class D is intialized with {self.specs}')

class E(D):
    def __init__(self, specs, dValue):
        super().__init__(specs, dValue)
        print(f'Class E has values {self.specs}, {self.dValue}')


specs, value, dValue = 'RTX 4060', 'Rs 425000', '34290000'

a = A(specs)
print(A.__mro__)
b = B(value)
print(B.__mro__)
c = C(specs, value)
print(C.__mro__)
d= D(specs, dValue)
print(D.__mro__)
e = E(specs, dValue)
print(E.__mro__)