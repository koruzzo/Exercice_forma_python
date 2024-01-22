import turtle
# pylint: disable=no-member
def etoile(distance):
    """..."""
    i = 0
    while i < 5:
        turtle.forward(distance)
        turtle.right(144)
        i += 1

    turtle.done()

etoile(500)
