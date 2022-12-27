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