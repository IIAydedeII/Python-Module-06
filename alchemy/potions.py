import elements
from .elements import create_air, create_earth


def healing_potion():
    return (
        f"Healing potion brewed with "
        f"'{create_earth()}' and '{create_air()}'"
    )


def strength_potion():
    return (
        f"Strength potion brewed with "
        f"'{elements.create_fire()}' and '{elements.create_water()}'"
    )
