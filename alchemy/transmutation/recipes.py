from ..elements import create_earth, create_air  # noqa
from ..potions import healing_potion, strength_potion  # noqa
from elements import create_fire, create_water  # noqa


def lead_to_gold():
    return ("Recipe transmuting Lead to "
            f"Gold: brew {create_air()} and {strength_potion()}"
            f" mixed with '{create_fire()}'")
