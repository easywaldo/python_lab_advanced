import math
import operator as op
from collections import ChainMap
from itertools import chain
from typing import Any, TypeAlias, NoReturn

Symbol: TypeAlias = str
Atom: TypeAlias = float | int | Symbol
Expression: TypeAlias = Atom | list


class Environment(ChainMap[Symbol, Any]):
    def change(self, key: Symbol, value: Any) -> None:
        for map in self.maps:
            if key in map:
                map[key] = value
                return
        raise KeyError(key)

inner_env = {'a': 2}
outer_env = {'a': 0, 'b': 1}
env = Environment(inner_env, outer_env)
print(env['a'])
print(env)

env['a'] = 111
env['c'] = 222

print(env)

env.change('b', 333)
print(env)

