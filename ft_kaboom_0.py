from alchemy.grimoire import light_spellbook

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    result = light_spellbook.light_spell_record("Lean", "water, earth, sprite")
    print(f"Testing record light spell: {result}")
