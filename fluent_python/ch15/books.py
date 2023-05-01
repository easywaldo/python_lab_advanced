import json
from typing import TYPE_CHECKING, TypedDict

class BookDict(TypedDict):
    isbn: str
    title: str
    authors: list[str]
    pagecount: int
    
AUTHOR_ELEMENT = '<AUTHOR>{}</AUTHOR>'

def to_xml(book: BookDict) -> str:
    elements: list[str] = []
    for key, value in book.items():
        if isinstance(value, list):
            elements.extend(
                AUTHOR_ELEMENT.format(n) for n in value)
        else:
            tag = key.upper()
            elements.append(f'<{tag}>{value}</{tag}>')
    xml = '\n\t'.join(elements)
    return f'<BOOK>\n\t{xml}\n</BOOK>'


book = BookDict(
        isbn='0134757599',
        title='Refactoring, 2e',
        authors=['Martin Fowler', 'Kent Beck'],
        pagecount=478
    )

print(to_xml(book=book))



authors = book['authors']
if TYPE_CHECKING:
    reveal_type(authors)
authors = 'Bob'
book['weight'] = 4.2
del book['title']

def from_json(data: str) -> BookDict:
    whatever: BookDict = json.loads(data)
    return whatever

json_str = """{"isbn": "091234123", "title": "good books", "authors": ["john", "hopkins"], "pagecount": 10}"""
print(from_json(json_str))


NOT_BOOK_JSON = """
        {"title": "Andromeda Strain",
         "flavor": "pistachio",
         "authors": true}
    """
    
not_book = from_json(NOT_BOOK_JSON)
if TYPE_CHECKING:
    reveal_type(not_book) # evealed type is "TypedDict('books.BookDict', {'isbn': builtins.str, 'title': builtins.str, 'authors': builtins.list[builtins.str], 'pagecount': builtins.int})"
    reveal_type(not_book['authors'])    # Revealed type is "builtins.list[builtins.str]"

print(not_book)
print(not_book['flavor'])   # Expression has type "Any"  , TypedDict "BookDict" has no key "flavor"

xml = to_xml(not_book)
print(xml)

