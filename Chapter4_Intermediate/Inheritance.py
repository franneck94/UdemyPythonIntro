class Animal:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def print_data(self):
        print("Height: ", self.height)
        print("Weight: ", self.weight)


class Dog(Animal):
    def __init__(self, weight, height):
        super().__init__(weight, height)

    def bark(self):
        print("Bark!")


class Cat(Animal):
    def __init__(self, weight, height):
        super().__init__(weight, height)

    def meow(self):
        print("Meow!")


def main():
    dog = Dog(10, 0.8)
    dog.print_data()
    dog.bark()

    cat = Cat(3, 0.3)
    cat.print_data()
    cat.meow()


if __name__ == "__main__":
    main()
