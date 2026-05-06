from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability


def main() -> None:
    print("Testing Creature with Healing Capability")
    print()

    heal_factory = HealingCreatureFactory()
    Sprou = heal_factory.create_base()
    bloo = heal_factory.create_evolved()
    print(Sprou.describe())
    print(Sprou.attack())
    if isinstance(Sprou, HealCapability):
        print(Sprou.heal())
    print()
    print(bloo.describe())
    print(bloo.attack())
    if isinstance(bloo, HealCapability):
        print(bloo.heal())

    print("\nTesting Creature with Transform Capability\n")

    trans_factory = TransformCreatureFactory()
    shif = trans_factory.create_base()
    Morph = trans_factory.create_evolved()
    print(shif.describe())
    print(shif.attack())
    if isinstance(shif, TransformCapability):
        print(shif.transform())
    print(shif.attack())
    if isinstance(shif, TransformCapability):
        print(shif.revert())
    print()
    print(Morph.describe())
    print(Morph.attack())
    if isinstance(Morph, TransformCapability):
        print(Morph.transform())
    print(Morph.attack())
    if isinstance(Morph, TransformCapability):
        print(Morph.revert())


if (__name__ == "__main__"):
    main()
