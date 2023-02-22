dict1 = {
    'a': 1
}
dict2 = {
    'b': 2
}

print('================================')
print(dict1 | dict2)

mydict = {'a': 1}
mydict |= {'a': 3, 'b': 4}
print(mydict)

other_dict = {'c': 99, 'd': 88}
print({**mydict, **other_dict})


mylist = [1,2,3,4,5]
print(*mylist)
def display(a, b, c, d, e):
    print(f'a, b, c, d, e are {a, b, c, d, e}')
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

display(*mylist)


my_func = lambda x: x**2
print(my_func(20))

MyClass = type("MyClass", (dict, ), {})
myc = MyClass(name="easywaldo")
print(myc)

user = {
    "first_name": (first_name := "John"),
    "last_name": (last_name := "Doe"),
    "display_name": f"{first_name} {last_name}",
    "height": (height := 168),
    "weight": (weight := 70),
    "bmi": weight / (height / 100) ** 2,
}
print(first_name, last_name, weight, height)


def concatenate(first: str, second: str, /, *, delim: str):
    return delim.join([first, second])

print(concatenate("John", "waldo", delim=" "))
# print(concatenate("John", "waldo", " "))    # TypeError: concatenate() takes 2 positional arguments but 3 were given

def concatenate(*items, delim: str):
    return delim.join(items)

print(concatenate("John", "Waldo", delim=" "))
print(concatenate("John", "Waldo", "easywaldo", delim=" "))
print(concatenate("easywaldo", delim=" "))


from graphlib import TopologicalSorter
table_ref = {
    "customers": set(),
    "accounts": {
        "customers"
    },
    "products": set(),
    "orders": {"accounts", "customers"},
    "order_products": {"orders", "products"},
}
sorter = TopologicalSorter(table_ref)
print(list(sorter.static_order()))