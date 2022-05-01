"""
Contextlib, __enter__, __exit__, exception
"""

"""
Context Manager : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할

가장 대표적인 with 구문 이해
정확한 이해 후 사용 >> 프로그래밍 개발해야 한다. (문제 발생의 요소가 될 수 있음)
"""

# Ex1
file = open('./testfile.txt', 'w')
try:
    file.write('Context manager text1\nContextlib Test1.')
finally:
    file.close()
    
# Ex2
with open('./testfile2.txt', 'w') as f:
    f.write('Context manager text2\nContextlib Test2.')
    
# Ex3
# Use Class => ContextManager with exception handling

class MyFileWriter():
    def __init__(self,file_name, method):
        print('my file writer started : __init__')
        self.file_obj = open(file_name, method)
    
    def __enter__(self):
        print('my file writer started : __enter__')
        return self.file_obj
    
    def __exit__(self, exc_type, exc_value, trace):
        print('my file writer started : __exit__')
        if exc_type:
            print(f'logging exception {exc_type} {exc_value} {trace}')
        self.file_obj.close()

with MyFileWriter('./testfile3.txt', 'w') as f:
    f.write('Context manager text3\nContextlib Test3.')