def numinput(prompt, test=0, maxtest=0, max=0, rec=0):
    global asd
    global jkl
    try:
        asd = float(input(prompt))
    except ValueError:
        print("enter a number!")
        if rec == 0:
            jkl = prompt + ". please enter a decimal number with out any letters around or any symbols or units. it should be in arabic numeral digits (0123456789). "
        numinput(jkl, test, maxtest, max, 1)
    if test == 1:
        if asd == 0 or asd<0:
            if rec == 0:
                jkl = prompt + ". please enter a whole number with out any letters around or any symbols or units. it should be in arabic numeral digits (0123456789). it should also be posotive.  "
            numinput(jkl, test, maxtest, max, 1)
    elif maxtest == 1:
        if asd <= max:
            if rec == 0:
                jkl = prompt + ". please enter a whole number with out any letters around or any symbols or units. it should be in arabic numeral digits (0123456789). it should also be posotive.  it should be less than " + max
            intinput(jkl, test, maxtest, max, 1)
    c = asd
    return c
        
def intinput(prompt, test=0, maxtest=0, max=0, rec=0):
    global asd
    global jkl
    try:
        asd = int(input(prompt))
        c = asd
    except ValueError:
        print("enter a number!")
        if rec == 0:
            jkl = prompt + ". please enter a decimal number with out any letters around or any symbols or units. it should be in arabic numeral digits (0123456789). "
        numinput(jkl, test, maxtest, max, 1)
    if test == 1:
        if asd == 0 or asd<0:
            if rec == 0:
                jkl = prompt + ". please enter a whole number with out any letters around or any symbols or units. it should be in arabic numeral digits (0123456789). it should also be posotive.  "
            numinput(jkl, test, maxtest, max, 1)
    elif maxtest == 1:
        if asd <= max:
            if rec == 0:
                jkl = prompt + ". please enter a whole number with out any letters around or any symbols or units. it should be in arabic numeral digits (0123456789). it should also be posotive.  it should be less than " + max
            intinput(jkl, test, maxtest, max, 1)
    c = asd
    return c
        