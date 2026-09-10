from .elements import create_earth, create_air  # noqa
from elements import create_fire, create_water  # noqa


def healing_potion():
    return f"'{create_earth()}' and '{create_air()}'"


def strength_potion():
    return f"'{create_fire()}' and '{create_water()}'"
