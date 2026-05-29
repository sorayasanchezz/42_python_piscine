class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def print_info(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, diameter: int) -> None:
        super().__init__(name, height, age)
        self.diameter = diameter

    def print_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.diameter}cm diameter")

    def produce_shade(self) -> None:
        shade = (self.height * self.diameter) // 320
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 season: str, nut_value: str) -> None:
        super().__init__(name, height, age)
        self.season = season
        self.nut_value = nut_value

    def print_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm,"
              f"{self.age} days, {self.season}")

    def nutritional_value(self) -> None:
        print(f"{self.name} is rich in {self.nut_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()

    rose = Flower("Rose", 25, 30, "red")
    rose.print_info()
    rose.bloom()
    print()

    tulip = Flower("Tulip", 35, 20, "yellow")
    tulip.print_info()
    tulip.bloom()
    print()

    oak = Tree("Oak", 500, 1825, 50)
    oak.print_info()
    oak.produce_shade()
    print()

    pine = Tree("Pine", 900, 3650, 40)
    pine.print_info()
    pine.produce_shade()
    print()

    tomato = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    tomato.print_info()
    tomato.nutritional_value()
    print()

    carrot = Vegetable("Carrot", 30, 70, "autumn harvest", "vitamin A")
    carrot.print_info()
    carrot.nutritional_value()
