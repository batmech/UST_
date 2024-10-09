# CONTEXT MANAGER

class Tester:
    def __init__(self,) -> None:
        # self.name = name
        # self.value = value
        print('Inside constructor!')
    
    def __enter__(self):
        print('Will you run first!')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print('Should end?')

with Tester() as cls:
    print('TEster')