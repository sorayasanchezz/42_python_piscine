from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if creature is None:
            return False
        return True

    def act(self, creature: Creature) -> list[str]:
        if self.is_valid(creature) is False:
            raise Exception("Creature is None")
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise Exception(
                 f"Invalid Creature '{creature.name}' "
                 "for this aggressive strategy")
        assert isinstance(creature, TransformCapability)
        return [creature.transform(), creature.attack(), creature.revert()]


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy")
        assert isinstance(creature, HealCapability)
        return [creature.attack(), creature.heal()]
