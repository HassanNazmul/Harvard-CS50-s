num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# total = round(num1 + num2)

# print("total of {0} and {1} is {2}".format(num1, num2, total))
# print(f"{total:,}")

"""
.format() is a built-in method in Python that allows us to format strings.
f-string is a built-in method in Python that allows us to format strings.

round() is a built-in method in Python that allows us to round a number to a specified number of digits.

, is a built-in method in Python that allows us to format numbers with commas.
"""

total = round(num1 / num2, 2)

# print(total)
print(f"{total:.2f}")

"""
2 is the number of digits after the decimal point.
:.2f is a built-in method in Python that allows us to format numbers with a specified number of digits after the decimal point.
"""