"""
RPG Game Characters System - Complete Project
==============================================

A comprehensive RPG game system demonstrating:
- Inheritance (character classes)
- Polymorphism (different attack styles)
- Composition (inventory, equipment)
- Encapsulation (stats management)

Run: python projects/game_characters/main.py
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from enum import Enum
import random


class ItemType(Enum):
    """Types of items."""
    WEAPON = "Weapon"
    ARMOR = "Armor"
    POTION = "Potion"
    MISC = "Miscellaneous"


class Item:
    """Base class for all items."""

    def __init__(self, name: str, item_type: ItemType, value: int):
        self.name = name
        self.item_type = item_type
        self.value = value

    def __str__(self):
        return f"{self.name} ({self.item_type.value}) - Value: {self.value} gold"


class Weapon(Item):
    """Weapon that increases attack power."""

    def __init__(self, name: str, damage: int, value: int):
        super().__init__(name, ItemType.WEAPON, value)
        self.damage = damage

    def __str__(self):
        return f"{self.name} (Weapon) - Damage: +{self.damage}, Value: {self.value}g"


class Armor(Item):
    """Armor that increases defense."""

    def __init__(self, name: str, defense: int, value: int):
        super().__init__(name, ItemType.ARMOR, value)
        self.defense = defense

    def __str__(self):
        return f"{self.name} (Armor) - Defense: +{self.defense}, Value: {self.value}g"


class Potion(Item):
    """Potion that restores health/mana."""

    def __init__(self, name: str, heal_amount: int, value: int):
        super().__init__(name, ItemType.POTION, value)
        self.heal_amount = heal_amount

    def use(self, character: 'Character'):
        """Use potion on character."""
        character.heal(self.heal_amount)
        return f"{character.name} used {self.name} and restored {self.heal_amount} HP!"

    def __str__(self):
        return f"{self.name} (Potion) - Heals: {self.heal_amount} HP, Value: {self.value}g"


class Inventory:
    """Manages character's inventory."""

    def __init__(self, max_slots: int = 20):
        self.max_slots = max_slots
        self.items: List[Item] = []
        self.gold = 0

    def add_item(self, item: Item) -> bool:
        """Add item to inventory."""
        if len(self.items) >= self.max_slots:
            return False

        self.items.append(item)
        return True

    def remove_item(self, item: Item) -> bool:
        """Remove item from inventory."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def has_item(self, item_name: str) -> bool:
        """Check if item exists."""
        return any(item.name == item_name for item in self.items)

    def get_item(self, item_name: str) -> Optional[Item]:
        """Get item by name."""
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def display(self):
        """Display inventory contents."""
        print(f"\n--- Inventory ({len(self.items)}/{self.max_slots}) ---")
        print(f"Gold: {self.gold}")
        if not self.items:
            print("  (Empty)")
        else:
            for item in self.items:
                print(f"  - {item}")


class Character(ABC):
    """Abstract base class for all characters."""

    def __init__(self, name: str, health: int, attack_power: int, defense: int):
        self.name = name
        self.max_health = health
        self.health = health
        self.base_attack = attack_power
        self.base_defense = defense
        self.level = 1
        self.experience = 0
        self.inventory = Inventory()
        self.equipped_weapon: Optional[Weapon] = None
        self.equipped_armor: Optional[Armor] = None

    @property
    def attack_power(self) -> int:
        """Total attack power including weapon."""
        weapon_damage = self.equipped_weapon.damage if self.equipped_weapon else 0
        return self.base_attack + weapon_damage

    @property
    def defense(self) -> int:
        """Total defense including armor."""
        armor_def = self.equipped_armor.defense if self.equipped_armor else 0
        return self.base_defense + armor_def

    def is_alive(self) -> bool:
        """Check if character is alive."""
        return self.health > 0

    def heal(self, amount: int):
        """Heal character."""
        old_health = self.health
        self.health = min(self.health + amount, self.max_health)
        healed = self.health - old_health
        print(f"{self.name} healed {healed} HP! ({old_health} → {self.health})")

    def take_damage(self, amount: int):
        """Take damage reduced by defense."""
        damage = max(1, amount - self.defense)  # Minimum 1 damage
        self.health = max(0, self.health - damage)
        print(f"{self.name} took {damage} damage! HP: {self.health}/{self.max_health}")

        if not self.is_alive():
            print(f"💀 {self.name} has been defeated!")

    def attack(self, target: 'Character'):
        """Basic attack."""
        damage = self.attack_power
        print(f"\n⚔️  {self.name} attacks {target.name}!")
        target.take_damage(damage)

    @abstractmethod
    def special_ability(self, target: 'Character'):
        """Special ability unique to each class."""
        pass

    def equip_weapon(self, weapon: Weapon):
        """Equip a weapon."""
        if self.equipped_weapon:
            self.inventory.add_item(self.equipped_weapon)

        if weapon in self.inventory.items:
            self.inventory.remove_item(weapon)

        self.equipped_weapon = weapon
        print(f"{self.name} equipped {weapon.name} (+{weapon.damage} attack)")

    def equip_armor(self, armor: Armor):
        """Equip armor."""
        if self.equipped_armor:
            self.inventory.add_item(self.equipped_armor)

        if armor in self.inventory.items:
            self.inventory.remove_item(armor)

        self.equipped_armor = armor
        print(f"{self.name} equipped {armor.name} (+{armor.defense} defense)")

    def gain_experience(self, xp: int):
        """Gain experience and level up if threshold reached."""
        self.experience += xp
        xp_needed = self.level * 100

        if self.experience >= xp_needed:
            self.level_up()

    def level_up(self):
        """Level up character."""
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.base_attack += 5
        self.base_defense += 3

        print(f"\n⭐ {self.name} leveled up to Level {self.level}!")
        print(f"   HP: {self.max_health}, ATK: {self.base_attack}, DEF: {self.base_defense}")

    def display_stats(self):
        """Display character stats."""
        print(f"\n{'='*50}")
        print(f"{self.name} - Level {self.level} {self.__class__.__name__}")
        print(f"{'='*50}")
        print(f"HP: {self.health}/{self.max_health}")
        print(f"Attack: {self.attack_power} (Base: {self.base_attack})")
        print(f"Defense: {self.defense} (Base: {self.base_defense})")
        print(f"Experience: {self.experience}")
        if self.equipped_weapon:
            print(f"Weapon: {self.equipped_weapon.name}")
        if self.equipped_armor:
            print(f"Armor: {self.equipped_armor.name}")
        print(f"{'='*50}")


class Warrior(Character):
    """Warrior class - high health, medium attack."""

    def __init__(self, name: str):
        super().__init__(name, health=150, attack_power=25, defense=15)
        self.rage = 0

    def special_ability(self, target: 'Character'):
        """Shield Block - reduce incoming damage for next attack."""
        print(f"\n🛡️  {self.name} activates Shield Block!")
        self.base_defense += 20
        print(f"Defense increased to {self.defense} for next attack!")

    def berserker_rage(self, target: 'Character'):
        """Powerful attack that costs health."""
        print(f"\n💢 {self.name} enters Berserker Rage!")
        damage = self.attack_power * 2
        self.health -= 10  # Cost
        print(f"{self.name} sacrifices 10 HP for a devastating blow!")
        target.take_damage(damage)


class Mage(Character):
    """Mage class - low health, high attack."""

    def __init__(self, name: str):
        super().__init__(name, health=80, attack_power=40, defense=5)
        self.mana = 100
        self.max_mana = 100

    def special_ability(self, target: 'Character'):
        """Cast Fireball - powerful magic attack."""
        mana_cost = 30
        if self.mana < mana_cost:
            print(f"{self.name} doesn't have enough mana!")
            return

        self.mana -= mana_cost
        print(f"\n🔥 {self.name} casts Fireball! (Mana: {self.mana}/{self.max_mana})")
        damage = self.attack_power + 20
        target.take_damage(damage)

    def heal_spell(self):
        """Cast healing spell."""
        mana_cost = 25
        if self.mana < mana_cost:
            print(f"{self.name} doesn't have enough mana!")
            return

        self.mana -= mana_cost
        heal_amount = 40
        self.heal(heal_amount)


class Archer(Character):
    """Archer class - medium health, medium attack, high speed."""

    def __init__(self, name: str):
        super().__init__(name, health=100, attack_power=30, defense=8)
        self.arrows = 20

    def special_ability(self, target: 'Character'):
        """Rapid Fire - multiple quick attacks."""
        if self.arrows < 3:
            print(f"{self.name} doesn't have enough arrows!")
            return

        self.arrows -= 3
        print(f"\n🏹 {self.name} uses Rapid Fire! (Arrows: {self.arrows})")

        for i in range(3):
            if target.is_alive():
                damage = self.attack_power // 2
                print(f"  Arrow {i+1}:")
                target.take_damage(damage)

    def critical_shot(self, target: 'Character'):
        """Chance for critical hit."""
        if self.arrows < 1:
            print(f"{self.name} is out of arrows!")
            return

        self.arrows -= 1
        print(f"\n🎯 {self.name} aims for a Critical Shot!")

        if random.random() < 0.6:  # 60% chance
            damage = self.attack_power * 2
            print("💥 CRITICAL HIT!")
            target.take_damage(damage)
        else:
            print("❌ Missed!")


class Enemy(Character):
    """Enemy character."""

    def __init__(self, name: str, health: int, attack: int, defense: int, xp_reward: int):
        super().__init__(name, health, attack, defense)
        self.xp_reward = xp_reward

    def special_ability(self, target: 'Character'):
        """Enemy special attack."""
        print(f"\n👹 {self.name} uses a special attack!")
        damage = self.attack_power * 1.5
        target.take_damage(int(damage))


class Battle:
    """Manages combat between characters."""

    def __init__(self, hero: Character, enemy: Enemy):
        self.hero = hero
        self.enemy = enemy
        self.turn = 1

    def execute_turn(self, attacker: Character, defender: Character, use_special: bool = False):
        """Execute one turn of combat."""
        if use_special:
            attacker.special_ability(defender)
        else:
            attacker.attack(defender)

    def fight(self):
        """Execute full battle."""
        print(f"\n{'='*60}")
        print(f"⚔️  BATTLE START: {self.hero.name} vs {self.enemy.name}")
        print(f"{'='*60}")

        while self.hero.is_alive() and self.enemy.is_alive():
            print(f"\n--- Turn {self.turn} ---")

            # Hero's turn
            print(f"\n{self.hero.name}'s turn:")
            action = random.choice(['attack', 'special'])
            self.execute_turn(self.hero, self.enemy, action == 'special')

            if not self.enemy.is_alive():
                break

            # Enemy's turn
            print(f"\n{self.enemy.name}'s turn:")
            self.execute_turn(self.enemy, self.hero, random.random() < 0.3)

            self.turn += 1

        # Battle result
        print(f"\n{'='*60}")
        if self.hero.is_alive():
            print(f"🎉 VICTORY! {self.hero.name} defeated {self.enemy.name}!")
            self.hero.gain_experience(self.enemy.xp_reward)
            print(f"Gained {self.enemy.xp_reward} XP!")

            # Loot
            loot_gold = random.randint(10, 50)
            self.hero.inventory.gold += loot_gold
            print(f"Found {loot_gold} gold!")
        else:
            print(f"💀 DEFEAT! {self.hero.name} was defeated by {self.enemy.name}...")

        print(f"{'='*60}\n")


def demo_game_system():
    """Demonstrate the complete game character system."""
    print("="*70)
    print("RPG GAME CHARACTER SYSTEM DEMO")
    print("="*70)

    # Create heroes
    print("\n--- Creating Heroes ---")
    warrior = Warrior("Conan the Brave")
    mage = Mage("Gandalf the Wise")
    archer = Archer("Legolas the Swift")

    # Display stats
    warrior.display_stats()

    # Equip items
    print("\n--- Equipping Items ---")
    iron_sword = Weapon("Iron Sword", 15, 50)
    leather_armor = Armor("Leather Armor", 10, 40)
    health_potion = Potion("Health Potion", 50, 25)

    warrior.inventory.add_item(iron_sword)
    warrior.inventory.add_item(leather_armor)
    warrior.inventory.add_item(health_potion)

    warrior.equip_weapon(iron_sword)
    warrior.equip_armor(leather_armor)

    warrior.display_stats()

    # Create enemies
    print("\n--- Creating Enemies ---")
    goblin = Enemy("Goblin Scout", 50, 15, 5, 50)
    orc = Enemy("Orc Warrior", 100, 25, 10, 100)

    # Battle 1
    print("\n--- Battle 1 ---")
    battle1 = Battle(warrior, goblin)
    battle1.fight()

    # Use potion
    print("\n--- Using Items ---")
    potion = warrior.inventory.get_item("Health Potion")
    if potion:
        print(potion.use(warrior))
        warrior.inventory.remove_item(potion)

    # Battle 2 with leveled character
    print("\n--- Battle 2 ---")
    battle2 = Battle(warrior, orc)
    battle2.fight()

    # Final stats
    warrior.display_stats()
    warrior.inventory.display()


if __name__ == "__main__":
    demo_game_system()
