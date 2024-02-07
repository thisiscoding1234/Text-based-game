import random as r
import ast


class room:
    def __init__(
        self, name: str, access: list, light: int, locked: int, desc: str
    ) -> None:
        self.name = name
        self.access = access
        self.light = light
        self.locked = locked
        self.desc = desc

    def __repr__(self) -> str:
        return f'room("{self.name}", {self.access}, {self.light}, {self.locked}, "{self.desc}") | '


def intal():
    with open("house.txt", "w") as file:
        x = [
            room("door", [1], 1, 0, "you are at the door"),
            room(
                "hall 0", [2, 3, 4, 5, 6, 0], 1, 0, "it is the hallway on the bottom floor"
            ),
            room("room 0-1", [1], 0, 0, "this is the first room"),
            room("stair 0-1", [1, 7], 0, 1, "it is the hallway on the bottom floor"),
            room("room 0-2", [1], r.randint(0, 1), r.randint(0, 1), "this is the 2 room"),
            room("room 0-3", [1], r.randint(0, 1), r.randint(0, 1), "this is the 3 room"),
            room("room 0-4", [1], r.randint(0, 1), r.randint(0, 1), "this is the 4 room"),
            room("hall 1", [8, 3], 1, 0, "this is the hallway on the first floor"),
            room("room 0-1", [7, 9], 0, 1, "this is the first room"),
            room("stairs", [8, 10], 1, 1, "this is the stairs"),
            room("End?", [9], 0, 1, "this is the End?"),
            "",
        ]

        a = str(x)
        t = len(str(x)) - 1
        c = a[1:t:]
        file.write(c)
    return "initialized house"


def get_room(num):
    with  open("house.txt", "r") as file:
        x = file.read()
        t = x.split(" | ,")
        return t[num]


def decode(l, get_acc=0, prev=0):
    print(l)
    rf = eval(str(l))
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

    if get_acc == 1:
        s = rf.access
    return s


def get_lock(l):
    rf = eval(str(l))
    c = rf.locked
    return c
