from typing import TypeVar
from collections.abc import Callable


a_string: str = 'value string'
a_integer: int = 123456
a_float: float = 1.23
a_boolean: bool = True
a_set: set = {1, 2, 3}
a_list: list = []
a_dict_1: dict = {}


def sum(x: int, y: int, z: float) -> float:
    return x + y + z


list_int: list[int] = [1, 2, 3, 4]
list_str: list[str] = ['a', 'b', 'c']
list_tuple: list[tuple] = [(1, 'a')]
list_list_int: list[list[int]] = [[1], [4, 5]]


a_dict_1: dict[str, int] = {
    "a": 1,
}

a_dict: dict[str, list[int]] = {
    'a': [1, 2],
    'b': [3, 4]
}


list_int = list[int]  # Type alias
dict_list_int = dict[str, list_int]


def sum_1(x: int, y: float | None = None) -> float:
    return x + y


sum_int = Callable[[int, int], int]


def executa(func: sum_int, a: int, b: int) -> int:
    return func(a, b)


def sum_exec(x: int, y: int) -> int:
    return x + y


T = TypeVar('T')


def get_item(list: list[T], index: int) -> T:
    return list[index]


list_int = get_item([1, 2, 3], 1)


class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    def say_my_name(person: Person) -> str:
        return person.full_name
