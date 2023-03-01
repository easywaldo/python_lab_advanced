import re
import reprlib


RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    

if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    
    for word in s:
        print(word)
        
    print(list(s))

    s3 = Sentence('Pig and Pepper')
    it = iter(s3)
    print(it)
    
    print('================================================================')
    print(next(it))
    print(next(it))
    print(next(it))
    # next(it)
    
    print(list(it))
    print(list(iter(s3)))
    
    
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        return SentenceIterator(self.words)
    
class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
        
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration("no more next elements")
        self.index += 1
        return word
    
    def __iter__(self):
        return self


print('================================================================')
s3 = Sentence('광진 초등학교 1학년')
it = iter(s3)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))