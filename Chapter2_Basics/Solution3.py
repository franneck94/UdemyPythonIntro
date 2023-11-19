"""Exercise 3:
1.)
Write a function that takes a dictionary as an input.
The function then iterates over all values and counts
how many "Students" are in the dictionary.
(See the dict "d" below)
2.)
Write a function that iterates over all key, value pairs
of the dictionary "d" and only print the name of the students.
"""


def exercise1(dct):
    num_students = 0
    for val in dct.values():
        if val == "Student":
            num_students += 1
    return num_students


def exercise2(dct):
    for key, val in dct.items():
        if val == "Student":
            print(key, "is a student")


d = {"Oskar": "Student", "Jan": "Instructor", "Thomas": "Student"}
print(exercise1(d))

exercise2(d)
