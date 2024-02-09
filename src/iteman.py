import random as r


class item:
    """ """

    def __init__(self, name: str, id: int, desc: str) -> None:
        self.name = name
        self.id = id
        self.desc = desc

    def __repr__(self) -> str:
        return f'item("{self.name}", {self.id}, "{self.desc}") | '


def intal():
    """
    Initializes the house by creating rooms and writing them to a file.

    Returns:
        str: A message indicating that the house has been initialized.
    """
    with open("inv.txt", "w", encoding="utf-8") as file:
        x = []

        a = str(x)
        t = len(str(x)) - 1
        c = a[1:t:]
        file.write(c)
    return "initialized house"


def get_item(num):
    """ """
    with open("inv.txt", "r", encoding="utf-8") as file:
        x = file.read()
        t = x.split(" | ,")
        return t[num]


def decode(obj):
    return "test"
