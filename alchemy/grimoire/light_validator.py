from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    for allowed in light_spell_allowed_ingredients():
        if allowed.casefold() in ingredients.casefold():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
