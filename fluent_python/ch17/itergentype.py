from keyword import kwlist
from typing import TYPE_CHECKING

short_kw = (k for k in kwlist if len(k) < 5)

if TYPE_CHECKING:
    reveal_type(short_kw)
    
long_kw = (k for k in kwlist if len(k) >= 4)

if TYPE_CHECKING:
    reveal_type(long_kw)
