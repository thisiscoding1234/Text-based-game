import argparse
import iteman as iman
import housmans as hman
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
    hman.intal()
    iman.intal()
name = input("what is your name: ")
print(f"welcome, {name}!")
ro = hman.get_room(0)
print(hman.decode(ro))
rm = 0

while True:
    cmd = input(''' 
Goto, inv, help, look, pickup.
What do you want to do?
''')
    if cmd == "goto":
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
            print("No that is not a room!")
    elif cmd == "inv":
        print(iman.get_player_list())
    elif cmd == "look":
        if hman.get_light(ro) == 0:
            print("The room is dark")
        else:
            print(iman.get_room(rm))
    elif cmd == "pickup":
        item = input("item: ")
        if item in iman.get_room(rm):
            iman.pickup(item)
        else:
            print("That item is not in this room!")
    elif cmd == "help":
        print("goto: go to a room")
        print("inv: view inventory")
        print("look: look around the room")
        print("help: view this message")
        print("pickup: pick up an item")
    else:
        print("I don't understand that command!")
print(f"goodbye, {name}!")
