import threading


def wrapped(timeout):
    user_input = None

    def get_input():
        nonlocal user_input
        user_input = input()

    input_thread = threading.Thread(target=get_input)
    input_thread.start()
    input_thread.join(timeout)

    if input_thread.is_alive():
        print("Time's up!")
        return None

    return user_input


def timed():
    user_input = wrapped(5)  # Wait for 5 seconds for user input
    if user_input is not None:
        return user_input
    return 0
