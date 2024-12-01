name = input("What is your name? ")

# if name == "Harry":
#     print("Griffindor")
# elif name == "Hermonie":
#     print("Griffindor")
# elif name == "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who? ")

# if name == "Harry" or name == "Hermonie" or name == "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who? ")

match name:
    case "Harry" | "Hermonie" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")

"""
match is a new feature in Python 3.10 and it is used to replace if-elif-else statements. It is more readable and easy to understand.
case is used to check the value of the variable.
case _ is used as a default case in match statement.
"""