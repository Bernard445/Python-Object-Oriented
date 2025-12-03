import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.shield_active = False

    def attack(self, opponent):
        if hasattr(opponent, "shield_active") and opponent.shield_active:
            print(f"{opponent.name}'s Magic Shield blocks the attack!")
            opponent.shield_active = False
            return
        damage = random.randint(max(0, self.attack_power - 10), self.attack_power + 10)
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        if self.health < self.max_health:
            self.health = self.health + 20
        if self.health > self.max_health:
            self.health = self.max_health

class Warrior(Character):
    def __init__(self, name, health=200, attack_power=50):
        super().__init__(name, health, attack_power)
        self.is_enraged = False  # track if rage mode is active

    def heavy_strike(self, opponent):
        """Powerful attack with bonus random damage."""
        bonus_damage = random.randint(15, 30)
        damage = self.attack_power + bonus_damage
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} uses Heavy Strike on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def rage(self):
        """Temporarily boost attack power for one attack."""
        if not self.is_enraged:
            self.attack_power += 10
            self.is_enraged = True
            print(f"{self.name} enters a rage! Attack power increased by 10 for the next attack!")
        else:
            print(f"{self.name} is already enraged!")

    def attack(self, opponent):
        # at the very start of Warrior.attack(self, opponent):
        if hasattr(opponent, "shield_active") and opponent.shield_active:
            print(f"{opponent.name}'s Magic Shield blocks the attack!")
            opponent.shield_active = False
            # consume rage even if the attack was blocked
            if self.is_enraged:
                self.attack_power -= 10
                self.is_enraged = False
                print(f"{self.name}'s rage fades. Attack power returns to normal.")
            return
        """Override attack to include rage reset."""
        # regular attack with random damage
        damage = random.randint(max(0, self.attack_power - 10), self.attack_power + 10)
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

        # if enraged, remove the bonus after this attack
        if self.is_enraged:
            self.attack_power -= 10
            self.is_enraged = False
            print(f"{self.name}'s rage fades. Attack power returns to normal.")

class Mage(Character):
    def __init__(self, name, health=100, attack_power=35,):
        super().__init__(name, health, attack_power,)

    def fireball(self, opponent):
        damage = random.randint(35, 55)
        print(f"{self.name} casts Fireball! Flames scorch {opponent.name} for {damage} damage!")
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def magicshield(self):
        self.shield_active = True
        print("Mage conjures a Magic Shield! The next attack will be blocked!")

class Archer(Character):
    def __init__(self, name, health=160, attack_power=45,):
        super().__init__(name, health, attack_power,)

    def rapidarrow(self, opponent):
        arrow1 = random.randint(20, 30)
        arrow2 = random.randint(20, 30) 
        opponent.health -= (arrow1 + arrow2)
        opponent.health = max(0, opponent.health)
        print(f"{self.name} fires two quick arrows! First hits for {arrow1}, second for {arrow2}. Total damage: {arrow1 + arrow2}.")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def evade(self):
        if random.random() < 0.75:
            self.shield_active = True
            print(f"{self.name} swiftly evades and prepares to dodge the next attack!")
        else:
            self.shield_active = False
            print(f"{self.name} tries to evade but fails!")

class Paladin(Character):
    def __init__(self, name, health=220, attack_power=40):
        super().__init__(name, health, attack_power)

    def holy_strike(self, opponent):
        """Holy attack with a small crit chance."""
        bonus = random.randint(15, 30)
        damage = self.attack_power + bonus
        # 20% crit chance: double final damage
        if random.random() < 0.20:
            damage *= 2
            print(f"{self.name} lands a CRITICAL Holy Strike!")
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} smites {opponent.name} for {damage} holy damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        """Guaranteed one-hit block (no chance to fail)."""
        self.shield_active = True
        print(f"{self.name} invokes Divine Shield! The next attack will be completely blocked.")

class EvilWizard(Character):
    def __init__(self, name, health=240, attack_power=35):
        super().__init__(name, health, attack_power)

    def regenerate(self):
        regen = random.randint(5, 15)
        self.health = min(self.max_health, self.health + regen)
        print(f"{self.name} regenerates {regen} HP! ({self.health}/{self.max_health})")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        # NEW: flag to control whether the wizard gets a turn after your action
        skip_enemy_turn = False

        if choice == '1':
            player.attack(wizard)

        elif choice == '2':
            # map abilities per class
            if isinstance(player, Warrior):
                sub = input("Choose ability: 1) Heavy Strike  2) Rage: ")
                if sub == '1':
                    player.heavy_strike(wizard)
                elif sub == '2':
                    player.rage()
                else:
                    print("Invalid choice.")

            elif isinstance(player, Mage):
                sub = input("Choose ability: 1) Fireball  2) Magic Shield: ")
                if sub == '1':
                    player.fireball(wizard)
                elif sub == '2':
                    player.magicshield()
                else:
                    print("Invalid choice.")

            elif isinstance(player, Archer):
                sub = input("Choose ability: 1) Rapid Arrow  2) Evade: ")
                if sub == '1':
                    player.rapidarrow(wizard)
                elif sub == '2':
                    player.evade()
                else:
                    print("Invalid choice.")

            elif isinstance(player, Paladin):
                sub = input("Choose ability: 1) Holy Strike  2) Divine Shield: ")
                if sub == '1':
                    player.holy_strike(wizard)
                elif sub == '2':
                    player.divine_shield()
                else:
                    print("Invalid choice.")

        elif choice == '3':
            before = player.health
            player.heal()
            healed = player.health - before
            if healed > 0:
                print(f"{player.name} heals {healed} HP! ({player.health}/{player.max_health})")
            else:
                print(f"{player.name} is already at full health.")

        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
            # NEW: viewing stats should NOT consume a turn
            skip_enemy_turn = True

        else:
            print("Invalid choice. Try again.")
            # if invalid, skip enemy turn so the player can choose again without penalty
            skip_enemy_turn = True

        # Enemy acts only if we didn't skip the turn and the wizard is still alive
        if not skip_enemy_turn and wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
