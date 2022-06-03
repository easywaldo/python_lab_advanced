from logging import Logger


class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(f'{self.__class__.__name__} {instance} {owner}')
        owner.n += 1
        return instance
    
class ClientClass:
    n: int = 0
    descriptor = DescriptorClass()
    

client = ClientClass()
client.descriptor
print(client.n)
