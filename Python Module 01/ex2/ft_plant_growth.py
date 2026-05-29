class Plant:

    """
    Growth: how many cm does it grow per day
    """

    def __init__(self, name: str, height: int, age: int, growth: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def grow(self) -> None:
        self.height += self.growth

    def age_up(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def one_day(plants: list[Plant]) -> int:
    cm_day = 0
    for plant in plants:
        plant.age_up()
        plant.grow()
        cm_day += plant.growth
    return cm_day


plants = [
    Plant("Rose", 25, 30, 1),
    # Plant("Cactus", 10, 120, 2),
    # Plant("Fern", 15, 20, 3),
]

days = 1
cm_plants = 0

while days < 8:
    if (days == 1 or days == 7):
        print(f"=== Day {days} ===")
        for plant in plants:
            print(plant.get_info())
    if days < 7:
        cm_plants += one_day(plants)
    days += 1
print(f"Growth this week: +{cm_plants}cm")
