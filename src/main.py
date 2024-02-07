import housmans as hman
import inputs as inp

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
        if rm not in hman.decode(ro, 1):
            print("Nice try, but you can't go there!")
            continue
        if hman.get_lock(hman.get_room(rm)) == 1:
            rm = prev
            print(
                "Nice try, but you can't go there, as the room is locked. Try and find a key to unlock it!"
            )
        ro = hman.get_room(rm)
        print(hman.decode(ro, 0, prev))
        if rm == 0:
            des = input("are you sure you want to leave? (y/n): ")
            if des == "y":
                break
            else:
                pass
    except IndexError:
        print("no!")

print(f"goodbye, {name}!")
