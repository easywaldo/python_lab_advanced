class Human:
    def __new__(cls, first_name=None):
        obj = super().__new__(cls)
        
        if first_name:
            obj.name= first_name
        else:
            obj.name = "Virat"
        
        print(type(obj))
        return obj
    
    
class Animal:
    def __new__(cls):
        obj = super().__new__(Human)
        print(f"Type of obj: {type(obj)}")
        return obj
    
if __name__ == "__main__":
    virat = Human()
    print(virat.name)
    sachin = Human("Sachin")
    print(sachin.name)
    
    print("================================================================")
    
    cat = Animal()
    type(cat)