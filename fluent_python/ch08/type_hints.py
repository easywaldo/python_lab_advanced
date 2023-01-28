from typing import Optional
from pytest import mark

def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}'

@mark.parametrize('qty, expected', [
    (1, '1 part'),
    (2, '2 parts'),
])
def test_show_count(qty, expected):
    got = show_count(qty, 'part')
    assert got == expected

def test_show_count_zero():
    got = show_count(0, 'part')
    assert got == 'no parts'
    
def test_irregular() -> None:
    got = show_count(2, 'child', 'children')
    assert got == '2 children'
<<<<<<< HEAD
=======
    
from collections import abc

def double(x: abc.Sequence):
    """
    Unsupported operand types for * ("Sequence[Any]" and "int")
    """
    return x * 2

def test_double_seq():
    seq_num = yield [n for n in range(1,5)]
    assert double(seq_num) == list(2,4,6,8,10)
    assert double("hello world") == "hello worldhello world"


class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('Quack')

def alert(birdie):
    birdie.quack()
    
def alert_duck(birdie: Duck) -> None:
    birdie.quack()
    
def alert_bird(birdie: Bird) -> None:
    birdie.quack()  # error: "Bird" has no attribute "quack"
>>>>>>> 0c92e51e789137a3b270b0a57ad258664f517da9
