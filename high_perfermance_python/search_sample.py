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


def binary_search(needle, haystack):
    imin, imax = 0, len(haystack)
    while True:
        if imin > imax:
            return -1
        midpoint = (imin + imax) // 2
        if haystack[midpoint] > needle:
            imax = midpoint
        elif haystack[midpoint] < needle:
            imin = midpoint+1
        else:
            return midpoint
        
result = binary_search(8, [1,2,3,4,5,6,7,8,9,10])
print(result)