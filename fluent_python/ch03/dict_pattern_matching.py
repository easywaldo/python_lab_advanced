def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'authors': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')
        
b1 = dict(
    api=1, 
    authors='Douglas Hosfstadter', 
    type='book', 
    title='Godel, Escher, Bach')

b2 = dict(
    api=2, 
    authors=['easywaldo', 'rosie', 'rucia'], 
    type='book', 
    title='Godel, Escher, Bach')
print(get_creators(b1))
print(get_creators(b2))