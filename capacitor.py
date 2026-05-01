from ex1.factory import HealingCreatureFactory, TransformCreatureFactory

def main() -> None:
    print("Testing Creature with Healing Capability")
    print()

    heal_factory = HealingCreatureFactory()
    Sprou = heal_factory.create_base()
    bloo = heal_factory.create_evolved()
    print(Sprou.describe())
    print(Sprou.attack())
    print(f"{Sprou.heal(Sprou)}\n")
    print(bloo.describe())
    print(bloo.attack())
    print(f"{bloo.heal(bloo)}\n")

    print("Testing Creature with Transform Capability\n")

    trans_factory = TransformCreatureFactory()
    shif = trans_factory.create_base()
    Morph = trans_factory.create_evolved()
    print(shif.describe())
    print(shif.attack())
    print(shif.transform(shif))
    print(shif.attack())
    print(shif.revert())
    print()
    print(Morph.describe())
    print(Morph.attack())
    print(Morph.transform(Morph))
    print(Morph.attack())
    print(Morph.revert())


if (__name__ == "__main__"):
    main()