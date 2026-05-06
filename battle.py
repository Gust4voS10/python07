from ex0.creatures import Creature
from ex0.factory import CreatureFactory, FlameFactory, AquaFactory


def pokeshowdown(factory: CreatureFactory) -> None:
    print("Testing factory")
    creat = factory.create_base()
    creat_evo = factory.create_evolved()
    print(creat.describe())
    print(creat.attack())
    print(creat_evo.describe())
    print(creat_evo.attack())


def battle(attacker: Creature, opponent: Creature) -> None:
    print("\nTesting battle")
    print(attacker.describe())
    print("            vs.")
    print(opponent.describe())
    print("          fight!")
    print(attacker.attack())
    print(opponent.attack())


if (__name__ == "__main__"):
    flame = FlameFactory()
    aqua = AquaFactory()
    pokeshowdown(flame)
    print()
    pokeshowdown(aqua)
    torchic = flame.create_base()
    popplio = aqua.create_base()
    battle(torchic, popplio)
