from typing import TypeVar, Generic

class Refuse:
    """"""
    
class Biodegradable(Refuse):
    """"""
    
class Compostable(Biodegradable):
    """"""
    
T_contra = TypeVar('T_contra', contravariant=True)

class TrashCan(Generic[T_contra]):
    def put(self, refuse: T_contra) -> None:
        pass
    
def deploy(trash_can: TrashCan[Biodegradable]):
    """"""
    
bio_can: TrashCan[Biodegradable] = TrashCan()
deploy(bio_can)

trash_can: TrashCan[Refuse] = TrashCan()
deploy(trash_can)

