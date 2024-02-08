import argparse

import housmans as hman
import inputs as inp

print("V 0.1.1α")

parser = argparse.ArgumentParser(prog="Text-Based-Game")

parser.add_argument("-d", "--debug", action="store_true")
parser.add_argument("-c", "--custom", action="store_true")
args = parser.parse_args()

if args.debug == True:
    print("Debug mode is on!")
elif args.custom == True:
    print("Custom mode is on!")

if args.custom is False:
    hman.intal()
name = input("what is your name: ")
print(f"welcome, {name}!")
ro = hman.get_room(0)
print(hman.decode(ro))
rm = 0

while True:
    try:
        prev = rm
        rm = inp.intinput("room num: ", 1, 1, 10)
        if rm not in hman.get_acc(ro):
            print("Nice try, but you can't go there!")
            continue
        if hman.get_lock(hman.get_room(rm)) == 1:
            rm = prev
            print(
                "Nice try, but you can't go there, as the room is locked. Try and find a key to unlock it!"
            )
        ro = hman.get_room(rm)
        print(hman.decode(ro))
        if rm == 0:
            des = input("are you sure you want to leave? (y/n): ")
            if des == "y":
                break
    except IndexError:
        print("no!")

print(f"goodbye, {name}!")
