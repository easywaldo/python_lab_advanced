from typing import cast

def find_first_str(a: list[object]) -> str:
    index = next(i for i, x in enumerate(a) if isinstance(x, str))
    return cast(str, a[index])

result = find_first_str("hello world")
print(result)

print(find_first_str(['hello world', 'python journey']))
# print(find_first_str([12, 45, 56, 678, 89, 99]))



def clip(text: str, max_len: int = 80) -> str:
    pass
print(clip.__annotations__)

from typing import get_type_hints
print(get_type_hints(clip))