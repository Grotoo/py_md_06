try:
    from alchemy.grimoire import dark_spellbook
    result = dark_spellbook.dark_spell_record("Shadow Curse", "bats, mud")
    print(result)
except ImportError as e:
    print("WAITTT *explosion* my laboratory noo! Circular import detected:")
    print(e)
