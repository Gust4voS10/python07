from ex2.strategy import NormalStrategy, AggressiveStrategy
from ex2.strategy import DefensiveStrategy, BattleStrategy
from ex0.factory import Creature, FlameFactory, AquaFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory


def battle(opponents: list[tuple[Creature, BattleStrategy]]) -> None:
    size: int = len(opponents)
    i: int = 0
    while (i < size):
        j: int = i + 1
        while (j < size):
            poke1: Creature = opponents[i][0]
            strat1: BattleStrategy = opponents[i][1]
            poke2: Creature = opponents[j][0]
            strat2: BattleStrategy = opponents[j][1]
            print(" * Battle *")
            print(poke1.describe())
            print("vs.")
            print(poke2.describe())
            print("now fight!")
            try:
                strat1.act(poke1, poke2)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            try:
                strat2.act(poke2, poke1)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            print("")
            j += 1
        i += 1


def main() -> None:
    fire_factory: FlameFactory = FlameFactory()
    water_factory: AquaFactory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    trans_factory = TransformCreatureFactory()

    flameling = fire_factory.create_base()
    aquabub = water_factory.create_base()
    sproutling = heal_factory.create_base()
    bloomelle = heal_factory.create_evolved()
    shiftling = trans_factory.create_base()

    normal: NormalStrategy = NormalStrategy()
    heal: DefensiveStrategy = DefensiveStrategy()
    aggressive: AggressiveStrategy = AggressiveStrategy()

    bt: list[list[tuple[Creature, BattleStrategy]]] = [[(flameling, normal),
                                                       (sproutling, heal)],
                                                      [(flameling, aggressive),
                                                       (sproutling, heal)],
                                                      [(aquabub, normal),
                                                       (sproutling, heal),
                                                       (shiftling, aggressive)]]
    for i, op in enumerate(bt):
        descriptions = ["basic", "error", "multiple"]
        print(f"Tournament {i} ({descriptions[i]})")
        print("[" + ", ".join(f"({creature.name}+{strategy.__class__.__name__.replace('Strategy', '')})" for creature, strategy in op) + "]")
        print("*** Tournament ***")
        print(f"{len(op)} opponents involved")
        try:
            battle(op)
        except Exception as e:
            print(e)


if (__name__ == "__main__"):
    main()