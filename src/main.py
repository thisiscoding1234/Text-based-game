"""
this is the main file for the text based game.
"""

import argparse
import time as t
import iteman as i_man
import housmans as h_man
import inputs as inp

print("V 0.1.1β")

parser = argparse.ArgumentParser(prog="Text-Based-Game")

parser.add_argument("-d", "--debug", action="store_true")
parser.add_argument("-c", "--custom", action="store_true")
args = parser.parse_args()

if args.debug is True:
    print("Debug mode is on!")
elif args.custom is True:
    print("Custom mode is on!")

if args.custom is False:
    h_man.initialise()
    i_man.initialise()
name = input("what is your name: ")
print(f"welcome, {name}!")
ro = h_man.get_room(0)
print(h_man.decode(ro))
RM = 0

while True:
    cmd = input(
        """
goto, inv, help, look, pickup, exit.
What do you want to do?
"""
    )
"""
    )
    if cmd == "goto":
        try:
            PRE = RM
            RM = inp.intinput("room num: ", 1, 1, 10)
            if RM not in h_man.get_acc(ro):
                print("Nice try, but you can't go there!")
                continue
            if h_man.get_lock(h_man.get_room(RM)) == 1:
                RM = PRE
                print(
                    "You can't go there, the room is locked! Try to find a key for it!"
                )
            ro = h_man.get_room(RM)
            print(h_man.decode(ro))
            if RM == 0:
                des = input("are you sure you want to leave? (y/n): ")
                if des == "y":
                    break
        except IndexError:
            print("No that is not a room!")
    elif cmd == "inv":
        print(i_man.get_player_list())
    elif cmd == "look":
        if h_man.get_light(ro) == 0:
            print("The room is dark")
        else:
            print(i_man.get_room(RM))
    elif cmd == "pickup":
        item = input("item: ")
        if item in i_man.get_room(RM):
            i_man.pickup(item)
        else:
            print("That item is not in this room!")
    elif cmd == "help":
        print("goto: go to a room")
        print("inv: view inventory")
        print("look: look around the room")
        print("help: view this message")
        print("pickup: pick up an item")
        print("exit: exit the game")
    elif cmd == "exit":
        break
    else:
        print("I don't understand that command!")
print(f"goodbye, {name}!")
if args.debug is False:
    t.sleep(5)
