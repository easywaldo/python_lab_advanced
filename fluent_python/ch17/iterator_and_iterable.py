# __iter__ 메서드를 구현한 클래스 예시
class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # iterator 객체를 반환하는 __iter__ 메서드
        return MyIterator(self.data)


# iterator 클래스 구현
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 다음 항목을 반환하고 인덱스를 증가시킴
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item


# MyIterable을 이용한 사용 예시
my_list = [1, 2, 3, 4, 5]
my_iterable = MyIterable(my_list)

for item in my_iterable:
    print(item)
