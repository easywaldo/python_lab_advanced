from collections.abc import Iterable
from itertools import zip_longest

FromTo = tuple[str, str]

def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text

from_to = (("hello", "greeting"), ("other", "my"), ("world", "family"))
print(zip_replace("hello other world", from_to))