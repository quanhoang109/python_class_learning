# RPG Game Characters System Project

A complete RPG game system demonstrating all major OOP concepts through an engaging game example.

## Features

### Character Classes
- **Warrior**: High HP (150), Medium ATK (25), High DEF (15)
  - Special: Shield Block (increases defense)
  - Rage: Berserker Rage (high damage, costs HP)

- **Mage**: Low HP (80), High ATK (40), Low DEF (5)
  - Special: Fireball (powerful magic attack, costs mana)
  - Utility: Heal Spell (restore HP, costs mana)

- **Archer**: Medium HP (100), Medium ATK (30), Medium DEF (8)
  - Special: Rapid Fire (3 quick attacks)
  - Utility: Critical Shot (chance for 2x damage)

### Item System
- **Weapons**: Increase attack power
- **Armor**: Increase defense
- **Potions**: Restore health
- **Inventory**: Manage items and gold

### Combat System
- Turn-based battles
- Normal and special attacks
- Experience and leveling
- Loot and rewards

## OOP Concepts Demonstrated

### 1. Inheritance
```
Character (abstract base)
├── Warrior
├── Mage
├── Archer
└── Enemy

Item (base)
├── Weapon
├── Armor
└── Potion
```

### 2. Polymorphism
- Each character class has unique `special_ability()` implementation
- Same method call, different behavior for each class
- Items have different effects when used

### 3. Composition
- Character **has** Inventory
- Inventory **has** Items
- Character can equip Weapon and Armor

### 4. Encapsulation
- Properties: `attack_power`, `defense` (calculated from base + equipment)
- Internal state management
- Controlled access to character stats

### 5. Abstraction
- Abstract `Character` class defines interface
- Each subclass implements required methods
- Battle system works with any Character type

## Class Diagram

```
┌─────────────────────┐
│  Character (ABC)    │
├─────────────────────┤
│ - name              │
│ - health            │
│ - base_attack       │
│ - base_defense      │
│ - level             │
│ - experience        │
│ - inventory         │
│ - equipped_weapon   │
│ - equipped_armor    │
├─────────────────────┤
│ + attack()          │
│ + take_damage()     │
│ + special_ability() │ (abstract)
│ + equip_weapon()    │
│ + equip_armor()     │
│ + level_up()        │
└──────────△──────────┘
           │
    ┌──────┴──────────┬──────────┐
    │                 │          │
┌───┴────┐     ┌──────┴────┐  ┌─┴──────┐
│Warrior │     │   Mage    │  │ Archer │
├────────┤     ├───────────┤  ├────────┤
│+ rage  │     │+ mana     │  │+arrows │
│        │     │           │  │        │
│+berserker()  │+fireball()│  │+rapid_ │
│        │     │+heal()    │  │ fire() │
└────────┘     └───────────┘  └────────┘

┌─────────────────────┐
│    Inventory        │
├─────────────────────┤
│ - items[]           │
│ - gold              │
│ - max_slots         │
├─────────────────────┤
│ + add_item()        │
│ + remove_item()     │
│ + get_item()        │
└─────────────────────┘

┌─────────────────────┐
│      Item           │
├─────────────────────┤
│ - name              │
│ - item_type         │
│ - value             │
└──────────△──────────┘
           │
    ┌──────┴────────┬────────┐
    │               │        │
┌───┴────┐    ┌────┴───┐ ┌─┴──────┐
│ Weapon │    │ Armor  │ │ Potion │
└────────┘    └────────┘ └────────┘
```

## Running the Project

```bash
python projects/game_characters/main.py
```

## Usage Example

```python
# Create character
warrior = Warrior("Conan")

# Equip items
sword = Weapon("Iron Sword", 15, 50)
armor = Armor("Plate Mail", 20, 100)

warrior.equip_weapon(sword)
warrior.equip_armor(armor)

# Create enemy
goblin = Enemy("Goblin", 50, 15, 5, 50)

# Battle
battle = Battle(warrior, goblin)
battle.fight()

# Use special abilities
warrior.special_ability(goblin)
warrior.berserker_rage(goblin)

# Level up and stats
warrior.display_stats()
```

## Combat Mechanics

### Turn Structure
1. Hero's turn (attack or special ability)
2. Enemy's turn (attack or special ability)
3. Check if either is defeated
4. Repeat until battle ends

### Damage Calculation
```python
actual_damage = max(1, attack_power - defense)
# Minimum 1 damage always dealt
```

### Experience and Leveling
- Gain XP by defeating enemies
- XP needed = level * 100
- On level up:
  - Max HP +20
  - Attack +5
  - Defense +3
  - HP restored to full

## Extension Ideas

1. **More Character Classes**: Add Rogue, Paladin, Necromancer
2. **Skills Tree**: Unlock new abilities as you level
3. **Status Effects**: Poison, burn, stun, freeze
4. **Equipment Rarities**: Common, Rare, Epic, Legendary
5. **Crafting System**: Combine items to create better ones
6. **Party System**: Control multiple characters
7. **Save/Load**: Persist game state
8. **Dungeon Crawler**: Navigate through rooms and encounter enemies
9. **Boss Battles**: Special mechanics for boss fights
10. **Quest System**: Complete quests for rewards
11. **Magic System**: Spell books and spell crafting
12. **Multiplayer**: PvP battles

## Design Patterns Used

- **Factory Pattern**: Creating different character and item types
- **Strategy Pattern**: Different combat strategies per class
- **Command Pattern**: Could be used for ability execution
- **Observer Pattern**: For battle event notifications
- **State Pattern**: Character states (normal, poisoned, buffed)

## Testing the System

Run the demo to see:
- Character creation and stats
- Equipment system
- Inventory management
- Turn-based combat
- Leveling system
- Special abilities for each class
- Victory and loot

```bash
python projects/game_characters/main.py
```

Expected flow:
1. Create warrior character
2. Equip weapon and armor
3. Battle goblin (easy)
4. Use healing potion
5. Battle orc (harder)
6. Level up during combat
7. Final stats display

## Learning Outcomes

By studying this project, you'll learn:
- How to design class hierarchies
- Property decorators for calculated values
- Composition vs inheritance
- Abstract base classes
- Polymorphic behavior
- Turn-based game mechanics
- State management
- Event-driven programming
