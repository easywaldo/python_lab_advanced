from typing import TYPE_CHECKING, TypedDict


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


def demo() -> None:
    book = BookDict(
        isbn='0134757599',
        title='Refactoring, 2e',
        authors=['Martin Fowler', 'Kent Beck'],
        pagecount=478
    )
    authors = book['authors']
    if TYPE_CHECKING:
        print('====')
        reveal_type(authors)
    authors = 'Bob'
    book['weight'] = 4.2
    del book['title']
    print(book)

if __name__ == '__main__':
    demo()
