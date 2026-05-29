from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy,
                 DefensiveStrategy, AggressiveStrategy)


Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory1, strategy1 = opponents[i]
                factory2, strategy2 = opponents[j]

                creature1 = factory1.create_base()
                creature2 = factory2.create_base()

                print("\n* Battle *")
                print(creature1.describe())
                print(" vs.")
                print(creature2.describe())
                print(" now fight!")

                for action in strategy1.act(creature1):
                    print(action)

                for action in strategy2.act(creature2):
                    print(action)

    except Exception as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    flame_factory: CreatureFactory = FlameFactory()
    aqua_factory: CreatureFactory = AquaFactory()
    healing_factory: CreatureFactory = HealingCreatureFactory()
    transform_factory: CreatureFactory = TransformCreatureFactory()

    normal: BattleStrategy = NormalStrategy()
    defensive: BattleStrategy = DefensiveStrategy()
    aggressive: BattleStrategy = AggressiveStrategy()

    print(
        "Tournament 0 (basic)\n"
        " [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (flame_factory, normal),
        (healing_factory, defensive)])

    print(
        "\nTournament 1 (error)\n"
        " [(Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (flame_factory, aggressive),
        (healing_factory, defensive)])

    print(
        "\nTournament 2 (multiple)\n"
        " [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (aqua_factory, normal),
        (healing_factory, defensive),
        (transform_factory, aggressive)])


if __name__ == "__main__":
    main()
