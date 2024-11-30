def main():
    x = int(input("Enter a number: "))
    print("The square of the number is", square(x))


def square(n):
    return pow(n, 2) # Pow is a built-in function that returns the value of x to the power of y


main()

