from tkinter.messagebox import NO
from typing import Optional


class LongNameDict(dict[str, int]):
    def longest_key(self) -> Optional[str]:
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


article_read = LongNameDict()
article_read['lucia'] = 8
article_read['easywaldo'] = 43
article_read['rosie'] = 42

print(article_read.longest_key())
