import random as r
import ast


class room:
    """
    A class representing a room in the game.

    Attributes:
        name (str): The name of the room.
        access (list): A list of access points to the room.
        light (int): The light level in the room.
        locked (int): The lock status of the room.
        desc (str): The description of the room.
    """

    def __init__(
        self, name: str, access: list, light: int, locked: int, desc: str
    ) -> None:
        self.name = name
        self.access = access
        self.light = light
        self.locked = locked
        self.desc = desc

    def __repr__(self) -> str:
        return f'room("
    {self.name}", {self.access}, {self.light}, {self.locked}, "{self.desc}") | '

def intal():
    """
    Initializes the house by creating rooms and writing them to a file.

    Returns:
        str: A message indicating that the house has been initialized.
    """
    with open("house.txt", "w") as file:
        x = [
            room(
                "door", [1], 1, 0, "you are at the door"
                ),
            room(
                "hall 0", [2, 3, 4, 5, 6, 0], 1, 0, "it is the hallway on the bottom floor"
            ),
            room(
                "room 0-1", [1], 0, 0, "this is the first room"
                ),
            room(
                "stair 0-1", [1, 7], 0, 1, "it is the hallway on the bottom floor"
                ),
            room(
                "room 0-2", [1], r.randint(0, 1), r.randint(0, 1), "this is the 2 room"
                ),
            room(
                "room 0-3", [1], r.randint(0, 1), r.randint(0, 1), "this is the 3 room"
                ),
            room(
                "room 0-4", [1], r.randint(0, 1), r.randint(0, 1), "this is the 4 room"
                ),
            room(
                "hall 1", [8, 3], 1, 0, "this is the hallway on the first floor"
                ),
            room(
                "room 0-1", [7, 9], 0, 1, "this is the first room"
                ),
            room(
                "stairs", [8, 10], 1, 1, "this is the stairs"
                ),
            room(
                "End?", [9], 0, 1, "this is the End?"
                ),
            "",
        ]

        a = str(x)
        t = len(str(x)) - 1
        c = a[1:t:]
        file.write(c)
    return "initialized house"


def get_room(num):
    """
    Retrieve the room at the specified index from the 'house.txt' file.

    Args:
        num (int): The index of the room to retrieve.

    Returns:
        str: The room at the specified index.

    """
    with open("house.txt", "r") as file:
        x = file.read()
        t = x.split(" | ,")
        return t[num]


def decode(list):
    """
    Decode the given input and return a formatted string describing the current location and its properties.

    Args:
        l (object): The input object to decode.
        prev (int, optional): The previous value. Defaults to 0.

    Returns:
        str: A formatted string describing the current location and its properties.
    """
    print(list)
    rf = eval(str(list))
    x = rf.desc
    i = rf.light
    c = rf.locked
    loc = rf.name

    if c == 1:
        x = "The door is locked. Try and find a key!"

    elif i == 0:
        x = "The room is dark. You can't see anything!"
    else:
        pass

    s = f"""
    you are in: {loc}, which is: {x}
    you can go to: {rf.access}
    """
    return s


def get_lock(list):
    """
    Returns the 'locked' attribute of the given object.

    Args:
        l: The object to retrieve the 'locked' attribute from.

    Returns:
        The value of the 'locked' attribute.

    """
    rf = eval(str(list))
    return rf.locked

def get_acc(l):
    """
    Returns the 'access' attribute of the given object.

    Args:
        l: The object to retrieve the 'access' attribute from.

    Returns:
        The value of the 'access' attribute.

    """
    rf = eval(str(l))
    return rf.access

def get_light(list):
    """
    Returns the 'light' attribute of the given object.

    Args:
        l: The object to retrieve the 'light' attribute from.

    Returns:
        The value of the 'light' attribute.

    """
    rf = eval(str(list))
    return rf.light

def get_desc(list):
    """
    Returns the 'desc' attribute of the given object.

    Args:
        l: The object to retrieve the 'desc' attribute from.

    Returns:
        The value of the 'desc' attribute.

    """
    rf = eval(str(list))
    return rf.desc

def get_name(list):
    """
    Returns the 'name' attribute of the given object.

    Args:
        l: The object to retrieve the 'name' attribute from.

    Returns:
        The value of the 'name' attribute.

    """
    rf = eval(str(list))
    return rf.name