def find_phonenumber(phonebook, name):
    for n, p in phonebook:
        if n == name:
            return p
    return None

phonebook = [
    ("John Doe", "123-456-7890"),
    ("Easywaldo", "999-999-9999"),
]

print(f"Easywaldo phone number is {find_phonenumber(phonebook, 'Easywaldo')}")

phonebook_dict = {
    "Easywaldo": "999-999-9999",
    "Thomas": "123-456-789",
}

print(f"Easywaldo phone number is {phonebook_dict['Easywaldo']}")

def list_unique_names(phonebook):
    unique_names = []
    for name, phonenumber in phonebook:
        first_name, last_name = name.split(" ", 1)
        for unique in unique_names:
            if unique == first_name:
                break
        else:
            unique_names.append(first_name)
    return len(unique_names)
    
def set_unique_names(phonebook):
    unique_names = set()
    for name, phonenumber in phonebook:
        first_name, last_name = name.split(" ", 1)
        unique_names.add(first_name)
    return len(unique_names)

phonebook = [
    ("John Doe", "999-999-9999"),
    ("Albert Einstein", "1234-211-1214"),
    ("Albert Rutherford", "8112-923-1924"),
    ("Guido van Rossum", "9201-234-1290"),
]

print("Number of unique names form set method:", set_unique_names(phonebook))
print("Number of unique names from list method: ", list_unique_names(phonebook))
