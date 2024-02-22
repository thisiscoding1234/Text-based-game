class item:
    """ """

    def __init__(self, name: str, loc: int, desc: str) -> None:
        self.name = name
        self.loc = loc
        self.desc = desc

    def __repr__(self) -> str:
        return f'item("{self.name}", {self.loc}, "{self.desc}") '


def intal():
    """
    Initializes the house by creating items in rooms and player's inventory and writing them to a file.

    Returns:
        str: A message indicating that the house has been initialized.
    """
    with open("h-inv.txt", "w", encoding="utf-8") as file:
        x = [
            item("key", 1, "a key..."),
            item("key", 2, "a key..."),
            item("key", 3, "a key..."),
            item("key", 4, "a key..."),
            item("Audio tape", 5, "a audio tape..."),
            item("key", 6, "a key..."),
            item("s", 7, "a d..."),
            item("d", 8, "a d..."),
            item("f", 9, "a d..."),
            item("v", 10, "a d..."),
        ]

        a = str(x)
        t = len(str(x)) - 1
        c = a[1:t:]
        file.write(c)
        with open("inv.txt", "w", encoding="utf-8") as file:
            x = [
                item("torch", -1, "a torch..."),
            ]
            a = str(x)
            t = len(str(x)) - 1
            c = a[1:t:]
            file.write(c)
    return "initialized house"


def get_item_list():
    with open("h-inv.txt", "r", encoding="utf-8") as file:
        x = file.read()
        t = x.split(" ,")
        return t

def get_player_list():
    with open("inv.txt", "r", encoding="utf-8") as file:
        x = file.read()
        t = x.split(" ,")
        return t


def get_room(num):
    f = []
    v = []
    t = get_item_list()
    for x in t:
        c = eval(x)
        if c.loc == num:
            f.append(c.name)
            f.append(c.desc)
            v.append(f)
        f = []
    return v

def pickup(l):
    t = get_item_list()
    p = get_player_list()
    for x in t:
        c = eval(x)
        if c.name == l:
            p.append(c)
            t.remove(x)
            with open("h-inv.txt", "w", encoding="utf-8") as file:
                a = str(t)
                t = len(str(t)) - 1
                c = a[1:t:]
                file.write(c)
            with open("inv.txt", "w", encoding="utf-8") as file:
                a = str(p)
                t = len(str(p)) - 1
                c = a[1:t:]
                file.write(c)
            return f"you picked up the {l}"
    return "item not found"