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


class AddressHolder:
    def __init__(self, street: str, city: str, state: str, code: str) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(
        self, name: str, email: str, phone: str, street: str, city: str, state: str, code: str) -> None:
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone
        
print(Friend.__mro__)


class BaseClass:
    num_base_calls = 0
    
    def call_me(self) -> None:
        print('Calling method on BaseClass')
        self.num_base_calls += 1
        
class LeftSubClass(BaseClass):
    num_left_calls = 0
    
    def call_me(self) -> None:
        BaseClass.call_me(self)
        print('Calling method on LeftSubClass')
        self.num_left_calls += 1
        
class RightSubClass(BaseClass):
    num_right_calls = 0
    
    def call_me(self) -> None:
        BaseClass.call_me(self)
        print('Calling method on RightSubClass')
        self.num_right_calls += 1
        
class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0
    
    def call_me(self) -> None:
        LeftSubClass.call_me(self)
        RightSubClass.call_me(self)
        print('Calling method on SubClass')
        self.num_sub_calls += 1
        
s = SubClass()
s.call_me()
print(s.num_sub_calls)
print(s.num_left_calls)
print(s.num_right_calls)
print(s.num_base_calls)




class BaseClass:
    num_base_calls = 0
    
    def call_me(self) -> None:
        print('Calling method on BaseClass')
        self.num_base_calls += 1
        
class LeftSubClass(BaseClass):
    num_left_calls = 0
    
    def call_me(self) -> None:
        BaseClass.call_me(self)
        print('Calling method on LeftSubClass')
        self.num_left_calls += 1
        
class RightSubClass(BaseClass):
    num_right_calls = 0
    
    def call_me(self) -> None:
        BaseClass.call_me(self)
        print('Calling method on RightSubClass')
        self.num_right_calls += 1
        
class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0
    
    def call_me(self) -> None:
        LeftSubClass.call_me(self)
        RightSubClass.call_me(self)
        print('Calling method on SubClass')
        self.num_sub_calls += 1
        
s = SubClass()
s.call_me()
print(s.num_sub_calls)
print(s.num_left_calls)
print(s.num_right_calls)
print(s.num_base_calls)