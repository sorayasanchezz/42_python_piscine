from ex0 import AquaFactory, FlameFactory, CreatureFactory


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(
        "Testing battle\n"
        f"{creature1.describe()} vs. {creature2.describe()}\n"
        "fight!\n"
        f"{creature1.attack()}\n"
        f"{creature2.attack()}")


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    creature_base = factory.create_base()
    creature_evolved = factory.create_evolved()

    print(creature_base.describe())
    print(creature_base.attack())

    print(creature_evolved.describe())
    print(creature_evolved.attack())


def main() -> None:
    aqua: CreatureFactory = AquaFactory()
    flame: CreatureFactory = FlameFactory()

    test_factory(flame)
    print()
    test_factory(aqua)
    print()
    test_battle(flame, aqua)


if __name__ == "__main__":
    main()
