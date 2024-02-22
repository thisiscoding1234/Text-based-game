class item:
    """
    Represents an item in the game.

    Attributes:
        name (str): The name of the item.
        loc (int): The location of the item.
        desc (str): The description of the item.
    """

    def __init__(self, name: str, loc: int, desc: str) -> None:
        self.name = name
        self.loc = loc
        self.desc = desc

    def __repr__(self) -> str:
        return f'item("{self.name}", {self.loc}, "{self.desc}") '


def intal():
    """
    Initializes the inventory files with default items.

    Returns:
        str: A message indicating that the house has been initialized.
    """
    with open("h-inv.txt", "w", encoding="utf-8") as file:
        x = [
            item("key", 1, "a key..."),
            item("key", 2, "a key..."),
            item("key", 3, "a key..."),
            item("key", 4, "a key..."),
            item("Audio tape", 5, "an audio tape..."),
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
    """
    Retrieves a list of items from the 'h-inv.txt' file.

    Returns:
        list: A list of items.
    """
    with open("h-inv.txt", "r", encoding="utf-8") as file:
        x = file.read()
        t = x.split(" ,")
        return t

def get_player_list():
    """
    Retrieves the player list from the 'inv.txt' file.

    Returns:
        list: A list containing the player items.
    """
    with open("inv.txt", "r", encoding="utf-8") as file:
        x = file.read()
        t = x.split(" ,")
        return t


def get_room(num):
    """
    Retrieve the items in a specific room.

    Args:
        num (int): The room number.

    Returns:
        list: A list of lists containing the name and description of each item in the room.
    """
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


def pickup(b):
    """
    Adds the specified item to the player's inventory and removes it from the item list.

    Args:
        l (str): The name of the item to be picked up.

    Returns:
        str: A message indicating whether the item was successfully picked up or not.
    """
    t = get_item_list()
    p = get_player_list()
    for x in t:
        c = eval(x)
        if c.name == b:
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
            return f"you picked up the {b}!"
    return "item not found"
