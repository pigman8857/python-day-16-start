# import another_module
#
# print(another_module.another_variable)
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.forward(50)
# timmy.right(45)
# timmy.forward(20)
# timmy.color("DeepPink2")
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)

# my_screen.exitonclick()

from prettytable import PrettyTable, TableStyle

table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
table.align = "l"

print(table)


