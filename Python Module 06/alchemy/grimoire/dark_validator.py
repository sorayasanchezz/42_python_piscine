from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()

    for allow in allowed:
        if allow.lower() in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
