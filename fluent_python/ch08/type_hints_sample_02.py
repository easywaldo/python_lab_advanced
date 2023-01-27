from typing import Union, List

def parse_token(token: str) -> Union[str, float]:
    try:
        return float(token)
    except ValueError:
        return token

print(parse_token("19.352"))


def tokenize(text: str) -> List[str]:
    return text.upper().split()

print(tokenize("hello world"))