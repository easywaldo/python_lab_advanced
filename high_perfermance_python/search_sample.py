# 파이썬은 2가지 유형의 배열 > 리스트, 튜플
# 튜플 : 고정적
# 리스트 : 가변적

def linear_search(needle, array):
    for i, item in enumerate(array):
        if item == needle:
            return i
    return -1

target_list = [1,2,3,45,6,100,99,12,387,5,634,43]
seek_value = 12

result = linear_search(seek_value, target_list)
print(result)