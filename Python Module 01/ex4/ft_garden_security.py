class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self._heigth = 0
        self._age = 0
        print(f"Plant created: {self.name}")

    def get_heigth(self) -> None:
        print(f"{self._heigth}")

    def get_age(self) -> None:
        print(f"{self._age}")

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print("Invalid operation attempted:"
                  f"height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = new_height
        print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print("Invalid operation attempted:"
                  f"age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = new_age
        print(f"Age updated: {self._age} days [OK]")

    def describe(self) -> None:
        print(f"Current plant: {self.name} "
              f"({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    # rose.set_age(-2)
    print()
    rose.describe()
