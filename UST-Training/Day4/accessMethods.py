class Student:
    def __init__(self, name, mark):
        self.name = name
        self.__marks = mark
    
    def studentInfo(self):
        print(f'Student name: {self.name}\nStudent marks; {self.__marks}\n')
        
    def studentChangeMarks(self, marks):
        self.__marks = marks

nibu = Student('Nibu', 97)
nibu.studentInfo()
nibu.studentChangeMarks(98)
nibu.studentInfo()

nibu._Student__marks = 99
nibu.studentInfo()