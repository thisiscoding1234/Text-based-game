"""
This module is used to force the user to enter an integer
"""


def intinput(prompt, test=0, maximum=0, top=0, rec=0):
    """
    Prompts the user to enter an integer and validates the input.

    Args:
        prompt (str): The prompt message to display to the user.
        test (int, optional): Flag to enable testing for numbers lees than 0
        maximum (int, optional): Flag to enable testing for numbers exceeding a max value.
        top (int, optional): The maximum value allowed for the input. Defaults to 0.

    Returns:
        int: The validated integer input.

    """
    try:
        asd = int(input(prompt))
        c = asd
    except ValueError:
        print("enter a number!")
        if rec == 0:
            jkl = (
                prompt
                + ". please enter a decimal"
                + " number without any letters around or any symbols or units. "
                + "it should be in arabic numeral digits (0123456789). "
            )
        intinput(jkl, test, maximum, top, 1)
    if test == 1:
        if asd == -1 or asd < -1:
            if rec == 0:
                jkl = (
                    prompt
                    + ". please enter a whole number without any letters"
                    + " around or any symbols or units."
                    + " it should be in arabic numeral digits (0123456789). "
                    + "it should also be positive.  "
                )
            intinput(jkl, test, maximum, top, 1)
    elif maximum == 1:
        if asd > top:
            if rec == 0:
                jkl = (
                    prompt
                    + ". please enter a whole number without any letters"
                    + " around or any symbols or units. it should be in"
                    + " arabic numeral digits (0123456789). "
                    + "it should also be positive.  it should be less than "
                    + top
                )
            intinput(jkl, test, maximum, top, 1)
    c = asd
    return c
