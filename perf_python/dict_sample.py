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

def list_unique_names(phonbook):
    unique_names = []
    for name, phonenumber in phonebook:
        first_name, last_name = name.split(" ", 1)
        for unique in unique_names:
            if unique == first_name:
                break
            else:
                unique_names.append(first_name)
        return len(unique_names)