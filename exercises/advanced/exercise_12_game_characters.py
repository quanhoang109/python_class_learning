"""
Exercise 12: Game Character System

Create an RPG character system:

Base class `Character`:
- Attributes: name, health, attack_power, defense
- Methods: take_damage(amount), attack(target), is_alive()

Child classes with DEFAULT STATS:
┌──────────┬────────┬──────────────┬─────────┐
│ Class    │ Health │ Attack Power │ Defense │
├──────────┼────────┼──────────────┼─────────┤
│ Warrior  │ 150    │ 20           │ 15      │
│ Mage     │ 80     │ 35           │ 5       │
│ Archer   │ 100    │ 25           │ 10      │
└──────────┴────────┴──────────────┴─────────┘

Special abilities:
- Warrior: shield_block() - temporarily doubles defense
- Mage: cast_spell(spell_name, target) - deals 1.5x attack damage
- Archer: rapid_fire(target) - attacks 3 times at 50% damage each

Class `Inventory`:
- Store items, add/remove items, display items

Add inventory system to characters.
"""

# TODO: Write your Character, Warrior, Mage, Archer, and Inventory classes here
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_items(self):
        return self.items
class Character:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.inventory = Inventory()
    def take_damage(self, amount):
        damage = max(0, amount - self.defense)
        self.health -= damage
        print(f"{self.name} takes {damage} damage! (HP left: {self.health})")
    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")
        target.take_damage(self.attack_power)
    def is_alive(self):
        return self.health > 0    
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20, defense=15)
    def shield_block(self):
        original_defense = self.defense
        self.defense *= 2
        print(f"{self.name} uses Shield Block! Defense is now {self.defense}.")
        return original_defense
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=35, defense=5)
    def cast_spell(self, spell_name, target):
        spell_damage = int(self.attack_power * 1.5)
        print(f"{self.name} casts {spell_name} on {target.name} for {spell_damage} damage.")
        target.take_damage(spell_damage)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=25, defense=10)
    def rapid_fire(self, target):
        for i in range(3):
            damage = int(self.attack_power * 0.5)
            print(f"{self.name} performs Rapid Fire attack {i+1} on {target.name} for {damage} damage.")
            target.take_damage(damage)

# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    print("=" * 60)
    print("GAME CHARACTER SYSTEM - TESTS")
    print("=" * 60)

    # ---------------------------------------------------------------------
    # Test 1: Character Creation with Default Stats
    # ---------------------------------------------------------------------
    print("\n--- Test 1: Character Creation ---")

    warrior = Warrior("Conan")
    mage = Mage("Gandalf")
    archer = Archer("Legolas")

    print(f"Warrior: {warrior.name} - HP:{warrior.health}, ATK:{warrior.attack_power}, DEF:{warrior.defense}")
    print(f"Mage: {mage.name} - HP:{mage.health}, ATK:{mage.attack_power}, DEF:{mage.defense}")
    print(f"Archer: {archer.name} - HP:{archer.health}, ATK:{archer.attack_power}, DEF:{archer.defense}")

    assert warrior.health == 150 and warrior.attack_power == 20 and warrior.defense == 15
    assert mage.health == 80 and mage.attack_power == 35 and mage.defense == 5
    assert archer.health == 100 and archer.attack_power == 25 and archer.defense == 10
    print("✓ All characters created with correct default stats!")

    # ---------------------------------------------------------------------
    # Test 2: Inventory - Add Items
    # ---------------------------------------------------------------------
    print("\n--- Test 2: Inventory - Add Items ---")

    warrior.inventory.add_item("Sword")
    warrior.inventory.add_item("Shield")
    warrior.inventory.add_item("Health Potion")

    mage.inventory.add_item("Staff")
    mage.inventory.add_item("Spellbook")
    mage.inventory.add_item("Mana Potion")

    archer.inventory.add_item("Bow")
    archer.inventory.add_item("Arrows x50")

    print(f"Warrior's inventory: {warrior.inventory.display_items()}")
    print(f"Mage's inventory: {mage.inventory.display_items()}")
    print(f"Archer's inventory: {archer.inventory.display_items()}")

    assert len(warrior.inventory.items) == 3
    assert len(mage.inventory.items) == 3
    assert len(archer.inventory.items) == 2
    assert "Sword" in warrior.inventory.items
    assert "Staff" in mage.inventory.items
    print("✓ Items added to inventory correctly!")

    # ---------------------------------------------------------------------
    # Test 3: Inventory - Remove Items
    # ---------------------------------------------------------------------
    print("\n--- Test 3: Inventory - Remove Items ---")

    print(f"Before: {warrior.inventory.display_items()}")
    warrior.inventory.remove_item("Health Potion")
    print(f"After removing Health Potion: {warrior.inventory.display_items()}")

    assert len(warrior.inventory.items) == 2
    assert "Health Potion" not in warrior.inventory.items

    # Try to remove non-existent item (should not crash)
    warrior.inventory.remove_item("Magic Ring")
    assert len(warrior.inventory.items) == 2
    print("✓ Items removed correctly! Non-existent item handled!")

    # ---------------------------------------------------------------------
    # Test 4: Inventory - Each Character Has Separate Inventory
    # ---------------------------------------------------------------------
    print("\n--- Test 4: Separate Inventories ---")

    # Create new characters
    hero1 = Warrior("Hero1")
    hero2 = Warrior("Hero2")

    hero1.inventory.add_item("Unique Sword")

    print(f"Hero1 inventory: {hero1.inventory.display_items()}")
    print(f"Hero2 inventory: {hero2.inventory.display_items()}")

    assert "Unique Sword" in hero1.inventory.items
    assert "Unique Sword" not in hero2.inventory.items
    assert len(hero2.inventory.items) == 0
    print("✓ Each character has separate inventory!")

    # ---------------------------------------------------------------------
    # Test 5: Basic Attack and Damage
    # ---------------------------------------------------------------------
    print("\n--- Test 5: Basic Attack ---")

    attacker = Warrior("Attacker")
    target = Mage("Target")

    initial_health = target.health
    attacker.attack(target)

    # Damage = attack_power - defense = 20 - 5 = 15
    expected_damage = attacker.attack_power - target.defense
    expected_health = initial_health - expected_damage

    print(f"Expected damage: {expected_damage}, Target health: {target.health}")
    assert target.health == expected_health
    print("✓ Basic attack works correctly!")

    # ---------------------------------------------------------------------
    # Test 6: Warrior Shield Block
    # ---------------------------------------------------------------------
    print("\n--- Test 6: Warrior Shield Block ---")

    tank = Warrior("Tank")
    enemy = Mage("Enemy")

    print(f"Original defense: {tank.defense}")
    original = tank.shield_block()
    print(f"Defense after shield block: {tank.defense}")

    assert tank.defense == 30  # 15 * 2
    assert original == 15

    # Restore defense
    tank.defense = original
    print(f"Defense restored: {tank.defense}")
    assert tank.defense == 15
    print("✓ Shield block works correctly!")

    # ---------------------------------------------------------------------
    # Test 7: Mage Cast Spell
    # ---------------------------------------------------------------------
    print("\n--- Test 7: Mage Cast Spell ---")

    wizard = Mage("Wizard")
    victim = Warrior("Victim")

    initial_health = victim.health
    wizard.cast_spell("Fireball", victim)

    # Spell damage = attack_power * 1.5 = 35 * 1.5 = 52
    # Actual damage = 52 - 15 (defense) = 37
    spell_damage = int(wizard.attack_power * 1.5)
    expected_damage = spell_damage - victim.defense
    expected_health = initial_health - expected_damage

    print(f"Spell power: {spell_damage}, After defense: {expected_damage}")
    print(f"Victim health: {victim.health}, Expected: {expected_health}")
    assert victim.health == expected_health
    print("✓ Cast spell works correctly!")

    # ---------------------------------------------------------------------
    # Test 8: Archer Rapid Fire
    # ---------------------------------------------------------------------
    print("\n--- Test 8: Archer Rapid Fire ---")

    sniper = Archer("Sniper")
    dummy = Mage("Dummy")

    initial_health = dummy.health
    sniper.rapid_fire(dummy)

    # Each hit = attack_power * 0.5 = 25 * 0.5 = 12
    # Damage per hit = 12 - 5 (defense) = 7
    # Total = 7 * 3 = 21
    damage_per_hit = int(sniper.attack_power * 0.5) - dummy.defense
    total_damage = damage_per_hit * 3
    expected_health = initial_health - total_damage

    print(f"Damage per hit: {damage_per_hit}, Total: {total_damage}")
    print(f"Dummy health: {dummy.health}, Expected: {expected_health}")
    assert dummy.health == expected_health
    print("✓ Rapid fire works correctly!")

    # ---------------------------------------------------------------------
    # Test 9: is_alive Check
    # ---------------------------------------------------------------------
    print("\n--- Test 9: is_alive Check ---")

    alive_char = Warrior("Alive")
    dead_char = Mage("Dead")

    print(f"Alive character (HP:{alive_char.health}): is_alive = {alive_char.is_alive()}")
    assert alive_char.is_alive() == True

    # Kill the character
    dead_char.health = 0
    print(f"Dead character (HP:{dead_char.health}): is_alive = {dead_char.is_alive()}")
    assert dead_char.is_alive() == False

    # Negative health
    dead_char.health = -10
    print(f"Overkilled character (HP:{dead_char.health}): is_alive = {dead_char.is_alive()}")
    assert dead_char.is_alive() == False
    print("✓ is_alive works correctly!")

    # ---------------------------------------------------------------------
    # Test 10: Full Battle Simulation
    # ---------------------------------------------------------------------
    print("\n--- Test 10: Full Battle Simulation ---")

    hero = Warrior("Hero")
    boss = Mage("Dark Wizard")

    # Give them items
    hero.inventory.add_item("Legendary Sword")
    hero.inventory.add_item("Health Potion x3")
    boss.inventory.add_item("Staff of Doom")

    print(f"\n=== BATTLE START ===")
    print(f"{hero.name}: HP={hero.health}, Items={hero.inventory.display_items()}")
    print(f"{boss.name}: HP={boss.health}, Items={boss.inventory.display_items()}")

    round_num = 1
    while hero.is_alive() and boss.is_alive():
        print(f"\n-- Round {round_num} --")

        # Hero uses shield block on odd rounds
        if round_num % 2 == 1:
            old_def = hero.shield_block()

        # Hero attacks
        hero.attack(boss)

        # Restore defense if shield was used
        if round_num % 2 == 1:
            hero.defense = old_def

        # Boss attacks if still alive
        if boss.is_alive():
            boss.cast_spell("Dark Bolt", hero)

        print(f"Status - {hero.name}: {hero.health} HP | {boss.name}: {boss.health} HP")
        round_num += 1

        # Safety limit
        if round_num > 20:
            print("Battle taking too long, ending...")
            break

    if hero.is_alive():
        print(f"\n{hero.name} WINS!")
    else:
        print(f"\n{boss.name} WINS!")

    print("✓ Battle simulation completed!")

    # ---------------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED!")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
