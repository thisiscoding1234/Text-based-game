""" this is the manager instance for the house """

import random as r

import iteman as iman


class Room:
    """
    A class representing a room in the game.

    Attributes:
        name (str): The name of the room.
        access (obj): A obj of access points to the room.
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
        return f'Room("{self.name}", {self.access}, {self.light}, {self.locked}, "{self.desc}") | '


def initialise():
    """
    Initializes the house by creating rooms and writing them to a file.

    Returns:
        str: A message indicating that the house has been initialized.
    """
    with open("house.txt", "w", encoding="utf-8") as file:
        x = [
            Room("door", [1], 1, 0, "you are at the door"),
            Room(
                "hall 0",
                [2, 3, 4, 5, 6, 0],
                1,
                0,
                "it is the hallway on the bottom floor",
            ),
            Room("room 0-1", [1], 0, 0, "this is the first room"),
            Room("stair 0-1", [1, 7], 0, 1, "it is the hallway on the bottom floor"),
            Room(
                "room 0-2", [1], r.randint(0, 1), r.randint(0, 1), "this is the 2 room"
            ),
            Room(
                "room 0-3", [1], r.randint(0, 1), r.randint(0, 1), "this is the 3 room"
            ),
            Room(
                "room 0-4", [1], r.randint(0, 1), r.randint(0, 1), "this is the 4 room"
            ),
            Room("hall 1", [8, 3], 1, 0, "this is the hallway on the first floor"),
            Room("room 0-1", [7, 9], 0, 1, "this is the first room"),
            Room("stairs", [8, 10], 1, 1, "this is the stairs"),
            Room("End?", [9], 0, 1, "this is the End?"),
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
    with open("house.txt", "r", encoding="utf-8") as file:
        x = file.read()
        t = x.split(" | ,")
        return t[num]


def decode(obj):
    """
    Decode input, return a formatted string describing location.
        Args:
            l (object): The input object to decode.
            prev (int, optional): The previous value. Defaults to 0.

        Returns:
            str: A formatted string describing the current location and its properties.
    """
    rf = eval(str(obj))
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


def get_lock(obj):
    """
    Returns the 'locked' attribute of the given object.

    Args:
        l: The object to retrieve the 'locked' attribute from.

    Returns:
        The value of the 'locked' attribute.

    """
    rf = eval(str(obj))
    return rf.locked


def get_acc(obj):
    """
    Returns the 'access' attribute of the given object.

    Args:
        l: The object to retrieve the 'access' attribute from.

    Returns:
        The value of the 'access' attribute.

    """
    rf = eval(str(obj))
    return rf.access


def get_light(obj):
    """
    Returns the 'light' attribute of the given object.

    Args:
        l: The object to retrieve the 'light' attribute from.

    Returns:
        The value of the 'light' attribute.

    """
    sd = iman.get_player_list()
    sety = set(sd)
    rf = eval(str(obj))
    flash = "torch" in sety
    if rf.light == 0 and flash is False:
        f = False
    else:
        f = True
    return f


def get_desc(obj):
    """
    Returns the 'desc' attribute of the given object.

    Args:
        l: The object to retrieve the 'desc' attribute from.

    Returns:
        The value of the 'desc' attribute.

    """
    rf = eval(str(obj))
    return rf.desc


def get_name(obj):
    """
    Returns the 'name' attribute of the given object.

    Args:
        l: The object to retrieve the 'name' attribute from.

    Returns:
        The value of the 'name' attribute.

    """
    rf = eval(str(obj))
    return rf.name
