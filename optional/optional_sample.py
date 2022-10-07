from typing import Optional
x: Optional[int] = None

# print(x + 5)


# mypy --no-implicit-optional ->> error
def foo(x: int = None) -> None:
    print(x)