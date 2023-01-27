from antigravity import geohash
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


from geolib import geohash as gh  # type: ignore

PRECISION = 9

def geohash(lat_lon: tuple[float, float]) -> str:
    return gh.encode(*lat_lon, PRECISION)

shanghai = (31.2304, 121.4737)
geohash(shanghai)