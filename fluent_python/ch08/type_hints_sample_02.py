from typing import Union


def parse_token(token: str) -> Union[str, float]:
    try:
        return float(token)
    except ValueError:
        return token

print(parse_token("19.352"))