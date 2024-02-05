import random as r
import ast

class room:
    def __init__(self, name: str, access: list, light:int, locked:int, desc:str ) -> None:
        self.name = name
        self.access = access
        self.light = light
        self.locked = locked
        self.desc = desc
        
    def __repr__(self) -> str:
        return f"room({self.name}, {self.access}, {self.light}, {self.locked}, {self.desc}) | "


def intal():
    file = open("house.txt", "w")
    x = [
        room("door", [1], 1, 0, "you are at the door"), 
        room("hall 0", [2, 4, 5, 6, 0], 1, 0, "it is the hallway on the bottom floor"),
        room("room 0-1", [1], 0, 0, "this is the first room"),
        room("stair 0-1", [1, 7], 0, 1, "it is the hallway on the bottom floor"),
        room("room 0-2", [1], r.randint(0,1), r.randint(0,1), "this is the 2 room"),
        room("room 0-3", [1], r.randint(0,1), r.randint(0,1), "this is the 3 room"),
        room("room 0-4", [1], r.randint(0,1), r.randint(0,1), "this is the 4 room"),
        room("hall 1", [1], 1, 0, "this is the hallway on the first floor"),
        room("room 0-1", [1], 0, 1, "this is the first room"),
        room("stairs", [1], 1, 1, "this is the stairs"),
        room("End?", [], 0, 1, "this is the End?"),
    ]

    a = str(x)
    t = len(str(x)) - 1
    c = a[1:t:]
    file.write(c)
    

def get_room(num):
    file = open("house.txt", "r")
    x = file.read()
    t = x.split(" | ,")
    print(x)
    return x[num]

def decode(l):
    s = f'''
    you are in: {a}, which is: {f}
    you can go to: {b}
    the light status is: {c}
    the locked status is: {d}
    '''
    
    return s