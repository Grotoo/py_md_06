from alchemy.potions import healing_potion, strength_potion

if __name__ == "__main__":
    print("=== Distillation ===")
    print(
        "Testing strength_potion:"
        f"Strength potion brewed with {strength_potion()}")
    print(
        "Testing healing_potion:"
        f"Healing potion brewed with {healing_potion()}")
    print()
