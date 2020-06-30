turtle1 = "a turtle"
turtle2 = "a turtle"

turtle1_alive = True
turtle2_alive = True

print(f'Turtle1 is currently: {turtle1_alive}\n##################\n')
print(f'Turtle2 is currently: {turtle2_alive}')


def game_over(dead_turtle):
    dead_turtle.color("yellow")


def is_alive():
    if turtle1_alive == False:
        game_over(turtle1)

    if turtle2_alive == False:
        game_over(turtle2)