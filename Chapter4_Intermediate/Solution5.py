"""Exercise 5:
1.)
Write a class Student that has the following member variables:
- Name (String)
- Lastname (String)
- Age (Integer)
- Id (Integer)
2.)
Write a method that prints the information about the student.
E.g. Student('Jan', 'Schaffranek', 28, 1080133228459) will print:
'Jan Schaffranek is 28 years old and has the id 1080133228459'
"""


# Exercise 1
class Student:
    def __init__(
        self,
        name: str,
        lastname: str,
        age: int,
        id: int,  # noqa: A002
    ) -> None:
        self.name = name
        self.lastname = lastname
        self.age = age
        self.id = id

    # Exercise 2
    def print_student(self) -> None:
        print(
            f"{self.name} {self.lastname} is {self.age} years"
            f" old and has the id {self.id}"
        )


def main():
    oskar = Student("Oskar", "Oskarson", 29, 1080132254623)
    oskar.print_student()
    jan = Student("Jan", "Schaffranek", 28, 1080133228459)
    jan.print_student()


if __name__ == "__main__":
    main()
