from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    for allowed in dark_spell_allowed_ingredients():
        if allowed.casefold() in ingredients.casefold():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
