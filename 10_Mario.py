def main():
    print_square(3)

# def print_square(size):
#     # Print a square of size x size
#     for i in range(size):
#         for j in range(size):
#             print("#", end="")
#         print()

def print_square(size):
    # Print a square of size x size
    for i in range(size):
        print("#" * size)

main()