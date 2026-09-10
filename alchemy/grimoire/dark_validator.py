from .dark_spellbook import dark_spell_allowed_ingredients  # noqa


def validate_dark_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()
    allowed_lower = [a.lower() for a in allowed]

    given = [i.strip().lower() for i in ingredients.split(",")]

    has_match = any(item in allowed_lower for item in given)

    if has_match:
        return (f"{ingredients} - VALID")
    else:
        return (f"{ingredients} - INVALID")
