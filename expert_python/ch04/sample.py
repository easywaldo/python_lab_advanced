from collections import UserDict
from typing import Any

class CaseInsentiveDict(UserDict):
    def __setitem__(self, key: str, value: Any):
        return super().__setitem__(key.lower(), value)
    
    def __getitem__(self, key: str) -> Any:
        return super().__getitem__(key.lower())
    
    def __delitem__(self, key: str) -> None:
        return super().__delitem__(key.lower())
    
headers = CaseInsentiveDict({
    "Content-Length": 30,
    "Content-Type": "application/json",
})
print(headers["CONTENT-LENGTH"])
print(headers["content-type"])
