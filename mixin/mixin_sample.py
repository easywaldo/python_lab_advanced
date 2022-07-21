class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token
    
    def __iter__(self):
        yield from self.str_token.split('-')
        
class UpperIterableMixin:
    def __iter__(self):
        return map(str.upper, super().__iter__())

class Tokenizer(UpperIterableMixin, BaseTokenizer):
    pass


tokenizer = BaseTokenizer("hello-world")
result = list(tokenizer)
print(result)


t2 = Tokenizer("hello-world")
r2 = list(t2)
print(r2)