class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        """ Función que crece """

        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    # hereda plant
    def __init__(self, name: str, height: int,
                 flower_color: str, blooming: bool) -> None:
        super().__init__(name, height)
        self.flower_color = flower_color
        self.blooming = blooming


class PrizeFlower(FloweringPlant):
    # hereda flowering (que esta hereda plant)
    def __init__(self, name: str, height: int, flower_color: str,
                 blooming: bool, prize_points: int) -> None:
        super().__init__(name, height, flower_color, blooming)
        self.prize_points = prize_points


class Garden:
    """ Maneja un jardín en concreto """

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.plants_added = 0
        self.total_growth = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        """ Crece cada planta del jardín y suelta un aviso """

        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()
            self.total_growth += 1

    def report(self, manager: "GardenManager") -> None:
        """ Muestra un informe por pantalla, paso el Garden y GardenManager """

        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:

            if isinstance(p, PrizeFlower):
                if not p.blooming:
                    print(f"- {p.name}: {p.height}cm, {p.flower_color} flowers"
                          f" (not blooming), Prize points: {p.prize_points}")
                else:
                    print(f"- {p.name}: {p.height}cm, {p.flower_color} flowers"
                          f" (blooming), Prize points: {p.prize_points}")

            elif isinstance(p, FloweringPlant):
                if not p.blooming:
                    print(f"- {p.name}: {p.height}cm, {p.flower_color} flowers"
                          " (not blooming)")
                else:
                    print(f"- {p.name}: {p.height}cm, {p.flower_color} flowers"
                          " (blooming)")

            else:
                print(f"- {p.name}: {p.height}cm")

        print(f"\nPlants added: {self.plants_added}, "
              f"Total growth: {self.total_growth}cm")
        regular, flowering, prize = manager.GardenStats.len_types(self)
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers")


class GardenManager:
    """ Contiene una lista con todos los jardínes """

    def __init__(self) -> None:
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        """ Guarda el nuevo garden dentro de self.gardens """

        self.gardens.append(garden)

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        """ Crea un manager y un Garden por cada owner """

        # manager = GardenManager()
        manager = cls()
        for o in owners:
            new_garden = Garden(o)
            manager.add_garden(new_garden)
        return manager

    def total_gardens(self) -> None:
        n = 0
        for g in self.gardens:
            n += 1
        print(f"Total gardens managed: {n}")

    class GardenStats:
        """ Clase anidada para stats """

        @staticmethod
        def len_types(garden: Garden) -> tuple[int, int, int]:
            """ Cuenta los tipos de plantas isinstance """

            len_regular = 0
            len_flowering = 0
            len_prize = 0
            for p in garden.plants:
                if isinstance(p, PrizeFlower):
                    len_prize += 1
                elif isinstance(p, FloweringPlant):
                    len_flowering += 1
                else:
                    len_regular += 1
            return len_regular, len_flowering, len_prize

        @staticmethod
        def validate_height(height: int) -> bool:
            return isinstance(height, int) and height > 0

        @staticmethod
        def garden_score(garden: Garden) -> int:
            height_sum = 0
            points = 0

            for p in garden.plants:
                height_sum += p.height
                if isinstance(p, PrizeFlower):
                    points += p.prize_points

            return height_sum + points + garden.total_growth


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    # Crea jardínes
    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    # Guardo referencia a los jardínes creados, para usarlos después
    alice_garden = manager.gardens[0]
    bob_garden = manager.gardens[1]

    # Crear plantas
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", True, 10)

    # Añadir plantas al jardín de Alice
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    print("")

    # Hacer crecer plantas
    alice_garden.help_plants_grow()

    print("")

    # Reporte
    alice_garden.report(manager)

    print("")

    # Validación de altura (utility)
    print(f"Height validation test: {manager.GardenStats.validate_height(10)}")

    # Scores
    alice_score = manager.GardenStats.garden_score(alice_garden)
    bob_score = manager.GardenStats.garden_score(bob_garden)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    # Total jardines
    manager.total_gardens()
