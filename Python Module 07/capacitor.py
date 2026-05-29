from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.creatures import Sproutling, Bloomelle, Shiftling, Morphagon


def test_heal_factory() -> None:
    print("Testing Creature with healing capability")

    factory = HealingCreatureFactory()
    base: Sproutling = factory.create_base()
    evolved: Bloomelle = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform_factory() -> None:
    print("Testing Creature with transform capability")

    factory = TransformCreatureFactory()
    base: Shiftling = factory.create_base()
    evolved: Morphagon = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    test_heal_factory()
    print()
    test_transform_factory()


if __name__ == "__main__":
    main()
