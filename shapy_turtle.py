"""
Turtle draws a picture based on the command string
the user inputs

assignment: Lab 4
file: shapy_turtle.py
author: Ryan Nowak
"""

import turtle as tt


def string_interpret(command):
    """
    string_interpret takes a string and interprets it based
    on the characters and numbers present

    :param command: command string that user input
    :return: returns nothing
    """
    while command != '' and command is not None:
        var = command[0]
        if var == '<':
            command = process_left(command)
        elif var == '>':
            command = process_right(command)
        elif var == 'S':
            command = process_s(command)
        elif var == 'T':
            command = process_t(command)
        elif var == 'C':
            command = process_c(command)
        elif var == 'F':
            command = process_f(command)
        elif var == 'B':
            command = process_b(command)
        elif var == 'U':
            command = process_u(command)
        elif var == 'D':
            command = process_d(command)
        elif var == 'R':
            command = process_r(command)
        elif var == 'P':
            command = process_p(command)
        elif var == 'G':
            command = process_g(command)
        elif var == 'Z':
            command = process_z(command)
        else:
            print("ERROR: Could not interpret ", command)
            return


def string_index(command):
    """
    string_index takes the command string and finds the index
    of the next non-numeric character

    :param command: command string
    :return: returns index of first non-numeric character. Returns
             none if it doesn't start with a number.
    """
    if not command[0].isdigit():
        return None
    for i in range(0, len(command)):
        if not command[i].isdigit():
            return i
    return len(command)


def process_left(command):
    """
    process_left turns the turtle left a number of degrees

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    if not st[0].isdigit():
        print("ERROR: Could not interpret ", command)
        return None
    idx = string_index(st)

    tt.left(int(st[:idx]))
    return st[idx:]


def process_right(command):
    """
    process_right turns the turtle right a number of degrees

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    if not st[0].isdigit():
        print("ERROR: Could not interpret ", command)
        return None
    idx = string_index(st)

    tt.right(int(st[:idx]))
    return st[idx:]


def process_s(command):
    """
    process_s has the turtle draw a square with a given side length

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    if not st[0].isdigit():
        print("ERROR: Could not interpret ", command)
        return None
    idx = string_index(st)

    length = int(st[:idx])
    for i in range(0, 4):
        tt.left(90)
        tt.forward(length)
    return st[idx:]


def process_t(command):
    """
    process_t has the turtle draw a triangle with side lengths obtained
    from command string

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    if not st[0].isdigit():
        print("ERROR: Could not interpret ", command)
        return None
    idx = string_index(st)

    length = int(st[:idx])
    for i in range(0, 3):
        tt.left(120)
        tt.forward(length)
    return st[idx:]


def process_c(command):
    """
    process_c has the turtle draw a circle with a radius obtained
    from command string

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    if not st[0].isdigit():
        print("ERROR: Could not interpret ", command)
        return None
    idx = string_index(st)

    tt.circle(int(st[:idx]))
    return st[idx:]


def process_f(command):
    """
    process_f has the turtle move forward a distance obtained
    from command string

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    if not st[0].isdigit():
        print("ERROR: Could not interpret ", command)
        return None
    idx = string_index(st)

    tt.forward(int(st[:idx]))
    return st[idx:]


def process_b(command):
    """
    process_b has the turtle move backward a distance obtained
    from command string

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    if not st[0].isdigit():
        print("ERROR: Could not interpret ", command)
        return None
    idx = string_index(st)

    tt.back(int(st[:idx]))
    return st[idx:]


def process_u(command):
    """
    process_f has the turtle put its pen up

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    idx = string_index(st)

    tt.up()
    return st[idx:]


def process_d(command):
    """
    process_d has the turtle put its pen down

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    idx = string_index(st)

    tt.down()
    return st[idx:]


def process_r(command):
    """
    process_r has the turtle draw a rectangle with a width and
    height obtained from the command string

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    if not st[0].isdigit():
        print("ERROR: Could not interpret ", command)
        return None
    idx = string_index(st)

    height = int(st[:idx])
    st = st[idx:]
    if st[0] == ',':
        st = st[1:]
        if not st[0].isdigit():
            print("ERROR: Could not interpret ", command)
            return None
        idx = string_index(st)
        width = int(st[:idx])

        tt.left(90)
        tt.forward(height)
        tt.left(90)
        tt.forward(width)
        tt.left(90)
        tt.forward(height)
        tt.left(90)
        tt.forward(width)

        return st[idx:]
    else:
        return None


def process_p(command):
    """
    process_p has the turtle draw a polygon with a number of sides and
    side length obtained from the command string

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    if not st[0].isdigit():
        print("ERROR: Could not interpret ", command)
        return None
    idx = string_index(st)

    sides = int(st[:idx])
    st = st[idx:]
    if st[0] == ',':
        st = st[1:]
        if not st[0].isdigit():
            print("ERROR: Could not interpret ", command)
            return None
        idx = string_index(st)
        length = int(st[:idx])

        for i in range(0, sides):
            tt.left(360 / sides)
            tt.forward(length)

        return st[idx:]
    else:
        return None


def process_g(command):
    """
    process_g has the turtle go to a location of x, y obtained from
    the command string

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    if not st[0].isdigit():
        print("ERROR: Could not interpret ", command)
        return None
    idx = string_index(st)

    x = int(st[:idx])
    st = st[idx:]
    if st[0] == ',':
        st = st[1:]
        if not st[0].isdigit():
            print("ERROR: Could not interpret ", command)
            return None
        idx = string_index(st)
        y = int(st[:idx])

        tt.goto(x, y)

        return st[idx:]
    else:
        return None


def process_z(command):
    """
    process_r changes the turtle pen color based on the integer
    obtained from the command string

    :param command: command string
    :return: modified command string
    """
    st = command[1:]
    if not st[0].isdigit():
        print("ERROR: Could not interpret ", command)
        return None
    idx = string_index(st)

    color = int(st[:idx])
    if color == 0:
        tt.pencolor('red')
    elif color == 1:
        tt.pencolor('blue')
    elif color == 2:
        tt.pencolor('green')
    elif color == 3:
        tt.pencolor('yellow')
    elif color == 4:
        tt.pencolor('brown')
    else:
        tt.pencolor('black')
    return st[idx:]


def main():
    """
    prompts the user for a command and then calls string_interpret
    with the command string
    """
    command = input("Enter command: ")
    string_interpret(command)
    print("Close canvas to exit program")
    tt.done()


if __name__ == '__main__':
    main()
