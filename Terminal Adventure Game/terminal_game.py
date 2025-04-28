"""
Terminal Adventure Game: A text-based RPG where the player explores, fights enemies,
and collects items to defeat a dragon.
"""

import random

PLAYER_NAME = "Jonathan"
PLAYER_HP = 100
PLAYER_ATTACK = 20
PLAYER_DEFENSE = 10
PLAYER_GOLD = 50
INVENTORY = []
EQUIPPED_WEAPON = None
WEAPON_DURABILITY = {"Sword": 0, "Axe": 0, "Bow": 0}  # Tracks durability points for each weapon
DRAGON_DEFEATED = False  # Add a global flag to track if the dragon has been defeated

def main_menu():
    """Display the main menu and handle user input."""
    print("\nWelcome to Jonathan's Dragon Slayer Adventure!")
    print("1. Explore the Forest")
    print("2. Climb the Mountain")
    print("3. Explore the Dungeon")
    print("4. Visit the Town")
    print("5. Enter the Dragon's Lair")
    if random.random() < 0.3:  # 30% chance the traveling merchant appears
        print("6. Visit the Traveling Merchant")
        merchant_available = True
    else:
        merchant_available = False
    print("7. Quit")
    choice = input("Choose an option: ")
    if choice == "6" and merchant_available:
        traveling_merchant()
    elif choice == "6" and not merchant_available:
        print("The Traveling Merchant is not here right now.")
    return choice

def explore_forest():
    """Handle the logic for exploring the forest."""
    print("\nYou venture into the forest...")
    encounter = random.choice(["enemy", "potion", "weapon", "rare_item", "nothing"])
    if encounter == "enemy":
        print("An enemy appears!")
        combat("Goblin", 30, 10)
    elif encounter == "potion":
        print("You found a healing potion!")
        heal(20)
    elif encounter == "weapon":
        weapon = random.choice(["Sword", "Axe", "Bow"])
        WEAPON_DURABILITY[weapon] += random.randint(5, 10)  # Add durability points
        print(f"You found {weapon} durability points! "
              f"Current {weapon} durability: {WEAPON_DURABILITY[weapon]}")
    elif encounter == "rare_item":
        rare_item = random.choice(["Golden Crown", "Ancient Relic", "Jeweled Dagger"])
        INVENTORY.append(rare_item)
        print(f"You found a rare item: {rare_item}! It has been added to your inventory.")
    else:
        print("The forest is quiet. Nothing happens.")

def traveling_merchant():
    """Handle interactions with the traveling merchant."""
    global PLAYER_GOLD
    print("\nThe Traveling Merchant has arrived!")
    print("1. Buy Sword Durability Pack (+10 durability, 50 gold)")
    print("2. Buy Axe Durability Pack (+10 durability, 50 gold)")
    print("3. Buy Bow Durability Pack (+10 durability, 50 gold)")
    print("4. Return to the main menu")
    choice = input("Choose an option: ")
    if choice == "1":
        if PLAYER_GOLD >= 50:
            PLAYER_GOLD -= 50
            WEAPON_DURABILITY["Sword"] += 10
            print(f"You bought a Sword Durability Pack! "
                  f"Current Sword durability: {WEAPON_DURABILITY['Sword']}")
        else:
            print("Not enough gold!")
    elif choice == "2":
        if PLAYER_GOLD >= 50:
            PLAYER_GOLD -= 50
            WEAPON_DURABILITY["Axe"] += 10
            print(f"You bought an Axe Durability Pack! "
                  f"Current Axe durability: {WEAPON_DURABILITY['Axe']}")
        else:
            print("Not enough gold!")
    elif choice == "3":
        if PLAYER_GOLD >= 50:
            PLAYER_GOLD -= 50
            WEAPON_DURABILITY["Bow"] += 10
            print(f"You bought a Bow Durability Pack! "
                  f"Current Bow durability: {WEAPON_DURABILITY['Bow']}")
        else:
            print("Not enough gold!")
    elif choice == "4":
        return
    else:
        print("Invalid choice.")

def town_merchant():
    """Handle interactions with the town merchant."""
    global PLAYER_GOLD, PLAYER_ATTACK
    while True:
        print("\nThe Town Merchant offers powerful upgrades and enchanted weapons!")
        print("1. Enchant Sword (+5 attack, 100 gold)")
        print("2. Enchant Axe (+10 attack, 150 gold)")
        print("3. Enchant Bow (+3 attack, 80 gold)")
        print("4. Sell rare items")
        print("5. Return to the town menu")
        choice = input("Choose an option: ")
        if choice == "1":
            if PLAYER_GOLD >= 100:
                PLAYER_GOLD -= 100
                PLAYER_ATTACK += 5  # Apply the upgrade to PLAYER_ATTACK
                print("Your Sword has been enchanted! It now deals +5 additional attack damage.")
            else:
                print("Not enough gold!")
        elif choice == "2":
            if PLAYER_GOLD >= 150:
                PLAYER_GOLD -= 150
                PLAYER_ATTACK += 10  # Apply the upgrade to PLAYER_ATTACK
                print("Your Axe has been enchanted! It now deals +10 additional attack damage.")
            else:
                print("Not enough gold!")
        elif choice == "3":
            if PLAYER_GOLD >= 80:
                PLAYER_GOLD -= 80
                PLAYER_ATTACK += 3  # Apply the upgrade to PLAYER_ATTACK
                print("Your Bow has been enchanted! It now deals +3 additional attack damage.")
            else:
                print("Not enough gold!")
        elif choice == "4":
            sell_rare_items()
        elif choice == "5":
            return
        else:
            print("Invalid choice.")

def sell_rare_items():
    """Allow the player to sell rare items."""
    global PLAYER_GOLD
    if not INVENTORY:
        print("You have no rare items to sell.")
        return
    print("\nYour rare items:")
    for i, item in enumerate(INVENTORY, 1):
        print(f"{i}. {item}")
    choice = input("Choose an item to sell (enter the number): ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(INVENTORY):
            item = INVENTORY.pop(index)
            item_value = random.randint(50, 150)  # Random gold value for the item
            PLAYER_GOLD += item_value
            print(f"You sold {item} for {item_value} gold! Current gold: {PLAYER_GOLD}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def visit_town():
    """Handle the logic for visiting the town."""
    global PLAYER_GOLD
    while True:
        print("\nYou arrive at the town.")
        print("1. Rest at the inn (+50 HP, 10 gold)")
        print("2. Buy a potion (10 gold)")
        print("3. View inventory")
        print("4. Equip a weapon")
        print("5. Visit the Town Merchant")  # New option for the town merchant
        print("6. Return to the main menu")
        choice = input("Choose an option: ")
        if choice == "1":
            if PLAYER_GOLD >= 10:
                PLAYER_GOLD -= 10
                heal(50)
                print(f"You rested at the inn. Remaining gold: {PLAYER_GOLD}")
            else:
                print("Not enough gold!")
        elif choice == "2":
            if PLAYER_GOLD >= 10:
                PLAYER_GOLD -= 10
                INVENTORY.append("Potion")
                print(f"You bought a potion! Remaining gold: {PLAYER_GOLD}")
            else:
                print("Not enough gold!")
        elif choice == "3":
            print(f"Inventory: {INVENTORY}")
        elif choice == "4":
            equip_weapon()
        elif choice == "5":
            town_merchant()
        elif choice == "6":
            return
        else:
            print("Invalid choice.")

def equip_weapon():
    """Allow the player to equip a weapon."""
    global EQUIPPED_WEAPON
    print("\nAvailable weapons with durability:")
    for weapon, durability in WEAPON_DURABILITY.items():
        print(f"{weapon}: {durability} durability points")
    if "God Gauntlet" in INVENTORY:
        print("God Gauntlet: Infinite durability (Legendary Weapon)")
    choice = input("Choose a weapon to equip (Sword, Axe, Bow, God Gauntlet): ").strip().lower()
    if choice == "god gauntlet" and "God Gauntlet" in INVENTORY:
        EQUIPPED_WEAPON = "God Gauntlet"
        print("You equipped the God Gauntlet. Prepare to unleash its legendary power!")
    elif choice.capitalize() in WEAPON_DURABILITY and WEAPON_DURABILITY[choice.capitalize()] > 0:
        EQUIPPED_WEAPON = choice.capitalize()
        print(f"You equipped the {EQUIPPED_WEAPON}.")
    elif choice.capitalize() in WEAPON_DURABILITY:
        print(f"Your {choice.capitalize()} has insufficient durability.")
    else:
        print("Invalid choice. Please select a valid weapon.")

def enter_dragons_lair():
    """Handle the logic for entering the dragon's lair."""
    global PLAYER_HP, DRAGON_DEFEATED  # Declare PLAYER_HP and DRAGON_DEFEATED as global
    print("\nYou enter the dragon's lair...")
    if DRAGON_DEFEATED:
        print("The dragon has already been defeated. The lair is now empty.")
        return  # Exit the function without starting combat

    print("The dragon roars and attacks!")
    dragon_special_attacks = ["Fire Breath", "Tail Swipe", "Wing Gust"]
    dragon_hp = 200  # Define the dragon's HP
    while PLAYER_HP > 0 and dragon_hp > 0:
        special_attack = random.choice(dragon_special_attacks)
        if special_attack == "Fire Breath":
            damage = random.randint(20, 40)
            PLAYER_HP -= damage
            print(f"The dragon uses Fire Breath! You take {damage} damage.")
        elif special_attack == "Tail Swipe":
            damage = random.randint(15, 30)
            PLAYER_HP -= damage
            print(f"The dragon uses Tail Swipe! You take {damage} damage.")
        elif special_attack == "Wing Gust":
            print("The dragon uses Wing Gust! You are knocked back and lose your next turn.")
            continue  # Skip the player's turn
        dragon_hp = combat("Dragon", dragon_hp, 30)  # Pass dragon_hp to combat and update it
    if PLAYER_HP > 0 and dragon_hp <= 0:
        print("\nCongratulations, Jonathan! You have slain the dragon and saved the kingdom!")
        print("As a reward, you receive the legendary God Gauntlet!")
        INVENTORY.append("God Gauntlet")  # Add the God Gauntlet to the inventory
        print("The God Gauntlet has been added to your inventory. It deals 200 damage with one punch!")
        print("You can now continue your adventure, but the dragon will no longer be defeatable.")
        DRAGON_DEFEATED = True  # Mark the dragon as defeated

def explore_dungeon():
    """Handle the logic for exploring the dungeon."""
    print("\nYou enter the dark dungeon...")
    encounter = random.choice(["enemy", "gold", "trap"])
    if encounter == "enemy":
        print("A skeleton warrior attacks!")
        combat("Skeleton Warrior", 40, 15)
    elif encounter == "gold":
        gold_found = random.randint(10, 50)
        global PLAYER_GOLD
        PLAYER_GOLD += gold_found
        print(f"You found {gold_found} gold! Total gold: {PLAYER_GOLD}")
    elif encounter == "trap":
        damage = random.randint(10, 30)
        global PLAYER_HP
        PLAYER_HP -= damage
        print(f"You triggered a trap and lost {damage} HP! Current HP: {PLAYER_HP}")

def climb_mountain():
    """Handle the logic for climbing the mountain."""
    print("\nYou climb the treacherous mountain...")
    encounter = random.choice(["enemy", "treasure", "nothing"])
    if encounter == "enemy":
        print("A mountain troll appears!")
        combat("Mountain Troll", 50, 20)
    elif encounter == "treasure":
        treasure = random.choice(["Golden Crown", "Magic Amulet"])
        INVENTORY.append(treasure)
        print(f"You found a {treasure}! It has been added to your inventory.")
    else:
        print("The mountain is peaceful. Nothing happens.")

def combat(enemy_name, enemy_hp, enemy_attack):
    """Handle the logic for combat."""
    global PLAYER_HP, PLAYER_GOLD, EQUIPPED_WEAPON
    print(f"\nCombat begins! You are fighting a {enemy_name}.")
    axe_cooldown = 0  # Tracks cooldown for the Axe
    while enemy_hp > 0 and PLAYER_HP > 0:
        print(f"\nYour HP: {PLAYER_HP} | {enemy_name}'s HP: {enemy_hp}")
        print(f"Your Gold: {PLAYER_GOLD} | Equipped Weapon: {EQUIPPED_WEAPON} | Weapon Durability: {WEAPON_DURABILITY}")
        print("1. Attack")
        print("2. Defend")
        print("3. Equip a new weapon")
        print("4. Run")
        choice = input("Choose an action: ")
        if choice == "1":
            if EQUIPPED_WEAPON == "God Gauntlet":
                damage = 200  # God Gauntlet deals massive damage
                print("You punch with the God Gauntlet, delivering a devastating blow!")
            elif EQUIPPED_WEAPON and WEAPON_DURABILITY[EQUIPPED_WEAPON] > 0:
                if EQUIPPED_WEAPON == "Sword":
                    damage = PLAYER_ATTACK + 10  # Sword adds moderate damage
                    if "enchanted" in INVENTORY:
                        damage += 5  # Enchantment bonus
                    print("You swing your sword swiftly!")
                elif EQUIPPED_WEAPON == "Axe":
                    if axe_cooldown == 0:
                        damage = PLAYER_ATTACK + 20  # Axe adds high damage
                        if "enchanted" in INVENTORY:
                            damage += 10  # Enchantment bonus
                        axe_cooldown = 1  # Set cooldown for the next turn
                        print("You swing your axe with great force!")
                    else:
                        damage = 0
                        axe_cooldown = 0  # Reset cooldown
                        print("Your axe is too heavy to swing again this turn!")
                elif EQUIPPED_WEAPON == "Bow":
                    damage = PLAYER_ATTACK + 5  # Bow adds low damage
                    if "enchanted" in INVENTORY:
                        damage += 3  # Enchantment bonus
                    print("You shoot an arrow from your bow!")
                WEAPON_DURABILITY[EQUIPPED_WEAPON] -= 1  # Reduce durability
                if WEAPON_DURABILITY[EQUIPPED_WEAPON] <= 0:
                    print(f"Your {EQUIPPED_WEAPON} broke!")
                    EQUIPPED_WEAPON = None
            else:
                damage = PLAYER_ATTACK  # Default attack
                print("You attack with your bare hands!")
            enemy_hp -= damage
            print(f"You attack the {enemy_name} for {damage} damage!")
        elif choice == "2":
            reduced_damage = max(enemy_attack - PLAYER_DEFENSE * 2, 0)
            PLAYER_HP -= reduced_damage
            counter_damage = PLAYER_DEFENSE
            enemy_hp -= counter_damage
            print(f"You defend! The {enemy_name} deals {reduced_damage} damage, and you counterattack for {counter_damage} damage!")
        elif choice == "3":
            equip_weapon()  # Allow equipping a new weapon during combat
            if EQUIPPED_WEAPON == "God Gauntlet":
                print("You equipped the God Gauntlet during combat!")
        elif choice == "4":
            print("You run away!")
            return enemy_hp  # Return the remaining HP of the enemy
        else:
            print("Invalid choice.")
            continue
        if enemy_hp > 0:
            if EQUIPPED_WEAPON == "Bow" and random.random() < 0.3:  # 30% chance enemy misses
                print(f"The {enemy_name} tries to attack but misses due to your ranged advantage!")
            else:
                PLAYER_HP -= enemy_attack
                print(f"The {enemy_name} attacks you for {enemy_attack} damage!")
    if PLAYER_HP <= 0:
        print("\nYou have been defeated...")
    elif enemy_hp <= 0:
        print(f"\nYou defeated the {enemy_name}!")
        gold_reward = random.randint(10, 30)
        PLAYER_GOLD += gold_reward
        print(f"You looted {gold_reward} gold from the {enemy_name}. Total gold: {PLAYER_GOLD}")
    return enemy_hp  # Return the remaining HP of the enemy

def heal(amount):
    """Heal the player by a specified amount."""
    global PLAYER_HP
    PLAYER_HP += amount
    print(f"You healed for {amount} HP. Current HP: {PLAYER_HP}")

def game_loop():
    """Main game loop."""
    while True:
        choice = main_menu()
        if choice == "1":
            explore_forest()
        elif choice == "2":
            climb_mountain()
        elif choice == "3":
            explore_dungeon()
        elif choice == "4":
            visit_town()
        elif choice == "5":
            enter_dragons_lair()
        elif choice == "7":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the game
game_loop()

