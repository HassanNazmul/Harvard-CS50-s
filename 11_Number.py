"""
try - is a block of code that will run if there is no exception
except - is a block of code that will run if there is an exception

ValueError - is raised when the built-in function for a data type has the valid type of argument, but the argument has an invalid value

while True - is an infinite loop
break - is used to exit a loop
pass - is used to prevent an error when an empty block is not allowed
"""

# try:
#     x = int(input("Enter a number: "))
#     print(x)
# except ValueError:
#     print("Invalid input.


# While loop to keep asking for a number until a number is entered
# while True:
#     try:
#         x = int(input("Enter a number: "))
#     except ValueError:
#         print("Invalid input. Please enter a number.")
#     else:
#         print(f"Your number is {x}")
#         break

# Function to keep asking for a number until a number is entered
def main():
    x = get_int()
    print(f"Your number is {x}")

def get_int():
    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            return x

main()