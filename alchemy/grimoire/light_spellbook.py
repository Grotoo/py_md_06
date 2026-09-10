from . import light_validator  # noqa


def light_spell_allowed_ingredients():
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str):
    result = light_validator.validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({result})"
