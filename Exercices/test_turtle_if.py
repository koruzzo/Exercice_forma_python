import turtle
# pylint: disable=no-member
wn = turtle.Screen()
my_art = turtle.Turtle()

for i in range(10):
    my_art.forward(50)
    if i % 2 == 0:
        my_art.left(72)
    else :
        my_art.right(144)
turtle.exitonclick()
