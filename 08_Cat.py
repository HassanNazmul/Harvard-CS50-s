# i = 3 # set i to 3

# while i != 0: # while i is not equal to 0
#     print("meow") # print meow
#     i = i - 1 # subtract 1 from i

# Output:
# meow
# meow
# meow

# i = 1 # set i to 1

# while i <= 3: # while i is less than or equal to 3
#     print("meow") # print meow
#     i = i + 1 # add 1 to i

# Output:
# meow
# meow
# meow

# i = 0 # set i to 0

# while i < 3: # while i is less than 3
#     print("meow") # print meow
#     i += 1 # add 1 to i

# Output:
# meow
# meow
# meow


####################################################################################################

# for _ in range(3): # for i in the range of 3
#     print("meow") # print meow

# # Output:
# # meow
# # meow
# # meow

"""
range is a function that returns a sequence of numbers.
_ is a variable name that is used when you don't need to use the variable in the loop.
"""

####################################################################################################

# while True:
#     n = int(input("What's n? ")) # ask the user for a number
#     if n <= 0:
#         continue # if n is less than or equal to 0, continue
#     else:
#         break # if n is greater than 0, break

# for _ in range(n): # for i in the range of n
#     print("meow") # print meow

"""
continue is a keyword that continues to the next iteration of the loop.
break is a keyword that exits the loop.
"""

####################################################################################################


def main():
    number = get_number() # call the get_number function and store the result in the number variable
    meow(number) # call the meow function with the number variable as an argument


def get_number(): # define the get_number function
    while True: # while True
        n = int(input("What's n? ")) # ask the user for a number
        if n <= 0: # if n is less
            continue 
        else:
            break

    return n # return n
        
def meow(n): # define the meow function with n as a parameter
    for _ in range(n): # for i in the range of n
        print("meow")

main() # call the main function