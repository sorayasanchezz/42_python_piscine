class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantEmptyName(GardenError):
    def __init__(self, message: str = "Plant name cannot be empty!") -> None:
        super().__init__(message)


class WaterLevelError(GardenError):
    pass


class SunlightError(GardenError):
    pass


class WaterTankError(GardenError):
    def __init__(self, message: str = "Not enough water in tank") -> None:
        super().__init__(message)


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plant(self, name: str) -> None:
        """Add plants to the list. If the name is empty, send an error"""

        if name == "":
            raise PlantEmptyName()
        self.plants.append(name)
        print(f"Added {name} successfully")

    def watering_system(self) -> None:
        """Water all plants in the list"""

        for p in self.plants:
            print(f"Watering {p} - success")

    def check_plant_health(self, name: str, water_level: int,
                           sunlight_hours: int) -> str:

        if water_level < 1:
            raise WaterLevelError(
                f"Water level {water_level} is too low (min 1)")

        if water_level > 10:
            raise WaterLevelError(
                f"Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise SunlightError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")

        if sunlight_hours > 12:
            raise SunlightError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")

        return (
            f"{name}: healthy (water: {water_level}, sun: {sunlight_hours})")

    def use_water_tank(self, amount: int) -> None:
        if amount > 10:
            raise WaterTankError()


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    # add valid plants and invalid plant
    plant_list = ["tomato", "lettuce", ""]
    garden = GardenManager()

    print("Adding plants to garden...")
    for p in plant_list:
        try:
            garden.add_plant(p)
        except PlantEmptyName as e:
            print(f"Error adding plant: {e}")

    # watering plants
    print("\nWatering plants...")
    try:
        print("Opening watering system")
        garden.watering_system()
    finally:
        print("Closing watering system (cleanup)")

    more_list = [
        ("tomato", 5, 8),
        ("lettuce", 15, 8)
    ]

    #  cheking plant health
    print("\nChecking plant health...")
    for name, water, sun in more_list:
        try:
            print(garden.check_plant_health(name, water, sun))
        except (WaterLevelError, SunlightError) as e:
            print(f"Error checking {name}: {e}")

    # continues to function despite the errors
    print("\nTesting error recovery...")
    try:
        garden.use_water_tank(20)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
