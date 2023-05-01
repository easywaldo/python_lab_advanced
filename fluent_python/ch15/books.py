from typing import TypedDict


class BookDict(TypedDict):
    """_summary_
    Args:
        TypedDict (_type_): _description_
    """
    isbn: str
    title: str
    authors: list[str]
    pagecount: int
    

pp = BookDict(title="programming Pearls",
                authors="Jon Bently",
                isbn="0101092012821",
                pagecount=256,)
print(pp)
print(type(pp))
# print(pp.title) # AttributeError: 'dict' object has no attribute 'title'
print(pp['title'])
print(pp.get('title'))
