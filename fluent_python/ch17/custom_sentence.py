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