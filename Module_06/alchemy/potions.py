def healing_potion() -> str:
    from alchemy.elements import create_fire, create_water
    return "Healing potion brewed with "
    + create_fire() + " and " + \
        create_water()


def strength_potion() -> str:
    from alchemy.elements import create_fire, create_earth
    return "Strength potion brewed with " + create_earth() + " and " + \
        create_fire()


def invisibility_potion() -> str:
    from alchemy.elements import create_air, create_water
    return "Invisibility potion brewed with " + create_air() + " and " + \
        create_water()


def wisdom_potion() -> str:
    from alchemy.elements import create_air, create_water, \
        create_earth, create_fire
    return "Wisdom potion brewed with all elements: "
    + create_air() + ", " + \
        create_water() + ", " + create_earth() + ", " + create_fire()
