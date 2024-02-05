import inputs as inp
import housmans as hman

hman.intal()

print("welcome")
ro = hman.get_room(0)
print(ro)
print(hman.decode(ro))

while True:
    try:
        rm = inp.intinput("room num: ", 1, 1, 10)
        ro = hman.get_room(rm)
        print(hman.decode(ro))
    except IndexError:
        print("no!")