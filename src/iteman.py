import random as r


class item:
    """ """

    def __init__(self, name: str, id: int, loc: int, desc: str) -> None:
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
        x = [
            item("key", 1, 2, "a key..."),
            item("key", 2, 4, "a key..."),
            item("key", 3, 5, "a key..."),
            item("key", 4, 6, "a key..."),
            item("Audio tape", 5, 8, "a audio tape..."),
            item("key", 6, 8, "a key..."),
            item("s", 7, 8, "a d..."),
            item("d", 8, 2, "a d..."),
            item("f", 9, 2, "a d..."),
            item("v", 10, 2, "a d..."),
        ]

        a = str(x)
        t = len(str(x)) - 1
        c = a[1:t:]
        file.write(c)
    return "initialized house"


def get_item_list():
    with open("inv.txt", "r", encoding="utf-8") as file:
        x = file.read()
        t = x.split(" | ,")
        return t


def get_pl():
    f = []
    t = get_item_list()
    for x in t:
        c = eval(x)
        if c.loc == -1:
            f.append(c.name)
            f.append(c.desc)
    return f


def get_room(num):
    f = []
    t = get_item_list()
    for x in t:
        c = eval(x)
        if c.loc == num:
            f.append(c.name)
            f.append(c.desc)
    return f


def pickup(l, id):
    return l[id]
