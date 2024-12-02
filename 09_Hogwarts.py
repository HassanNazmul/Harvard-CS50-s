# students = ["Harry", "Ron", "Hermione", "Ginny", "Draco", "Neville", "Luna"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Gryffindor", "Slytherin", "Gryffindor", "Ravenclaw"]

# # Print the list of students
# for i in range(len(students)):
#     print( i + 1, students[i])

"""
range - is used for a list of numbers. It is used to generate a sequence of numbers.
len - is used to get the length of a list. It is used to get the number of elements in a list.
i + 1 - is used to print the index of the list starting from 1.

dict - is used to store data in key-value pairs.
sep - is used to separate the values in the print statement.
"""

# Using Dictionary
# students = {
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Hermione": "Gryffindor",
#     "Ginny": "Gryffindor",
#     "Draco": "Slytherin",
#     "Neville": "Gryffindor",
#     "Luna": "Ravenclaw"
# }
#
# # Print the list of students
# for student in students:
#     print(student, students[student], sep=" is in ")

# Using List of Dictionaries
students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "jack russell terrier"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Ginny", "house": "Gryffindor", "patronus": "horse"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}, # None is a special value in Python
    {"name": "Neville", "house": "Gryffindor", "patronus": "hare"},
    {"name": "Luna", "house": "Ravenclaw", "patronus": "hare"}
]

for student in students:
    print(student["name"], "is in", student["house"], "and their patronus is", student["patronus"])