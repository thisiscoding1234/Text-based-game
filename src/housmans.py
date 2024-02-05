import random as r

def intal():
    f = open("house.txt", "w")
    x = [["door", [1], 1, 0, "you are at the door"],5, 
        ["hall 0", [2, 4, 5, 6, 0], 1, 0, "it is the hallway on the bottom floor"],5,
        ["room 0-1", [1], 0, 0, "this is the first room"],5,
        ["stair 0-1", [1, 7], 0, 1, "it is the hallway on the bottom floor"],5,
        ["room 0-2", [1], r.randint(0,1), r.randint(0,1), "this is the 2 room"],5,       
        ["room 0-3", [1], r.randint(0,1), r.randint(0,1), "this is the 3 room"],5,
        ["room 0-4", [1], r.randint(0,1), r.randint(0,1), "this is the 4 room"],5,
        ["hall 1", [1], 1, 0, "this is the hallway on the first floor"],5,
        ["room 0-1", [1], 0, 1, "this is the first room"],5,
        ["stair", [1], 1, 1, "this is the stairs"],5,
        ["End?", [1], 0, 1, "this is the End?"],5,
        ]
    a = str(x)
    t = len(str(x)) - 1
    c = a[1:t:]
    f.write(c)
    

def get_room(num):
    f = open("house.txt", "r")
    x = f.read()
    t = x.split(", 5,")
    return t[num]

def decode(list):
    print(list)
    g = list
    a = g[0]
    b = g[1]
    c = g[2]
    d = g[3]
    f = g[4]
    
    s = f'''
    you are in: {a}, which is: {f}
    you can go to: {b}
    the light status is: {c}
    the locked status is: {d}
    '''
    
    return s