from __future__ import annotations


class ContactList(list["Contact"]):
    def search(self, name: str) -> list["Contact"]:
        matching_contacts: list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}" f")"
        )

c1 = Contact("easywaldo", "easywaldo@gmail.com")
c2 = Contact("john", "john@gmail.com")
c2 = Contact("tom", "tom@gmail.com")

result = [c.name for c in Contact.all_contacts.search('john')]
print(result)



class Friend(Contact):
    """_summary_
    Args:
        Contact (_type_): _description_
    """
    def __init__(self, name: str, email: str, phone: str) -> None:
        super().__init__(name, email)
        self.phone = phone
