import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:
    
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'
    
    def __iter__(self):
        for word in self.words:
            yield word
    

language_list = Sentence('Python Kotlin C# Java PHP Javascript SQL Go Typescript C++ VisualBasic')
for lang in language_list:
    print(lang)
    
    
numbers = [1,2,3,4,5,6,7,8,9,10]
n_iter = iter(numbers)
print(next(n_iter))
print(next(n_iter))
print(next(n_iter))
print(next(n_iter))
print(next(n_iter))

class Student:
    def __init__(self, name):
        self.name = name

class Classroom:
    def __init__(self, students):
        self.students = students
        
    def __iter__(self):
        for student in self.students:
            yield student
            
class_room = Classroom([Student(name="easywaldo"), Student(name="romeo")])
for student in class_room:
    print(student.name)
