import random
import time
from os import system


class Player:
    def __init__(self, name, HP=100):
        self.name = name
        self.HP = HP
        self.weapons = {
            "Hand": Weapon("Hand", 1, 10),
            "Sword": Weapon("Sword", 30, 50),
            "Bow": Weapon("Bow", 60, 80)
        }
        self.current_weapon = None

    def player_choose_weapon(self):
        print("\nChoose your weapon:")
        for idx, weapon in enumerate(self.weapons.keys(), start=1):
            print(f"{idx}. {weapon}")
        choice = input("Enter weapon number: ")
        try:
            choice_idx = int(choice)
            if 1 <= choice_idx <= len(self.weapons):
                self.current_weapon = list(self.weapons.values())[choice_idx - 1]
                print(f"You chose {self.current_weapon.name}.")
            else:
                print("Invalid choice. Please try again.")
                self.choose_weapon()
        except ValueError:
            print("Invalid choice. Please enter a number.")
            self.choose_weapon()

    def attack(self, target):
        if not self.current_weapon:
            print("You need to choose a weapon!")
            return
        print(f"\n{self.name} attacks with {self.current_weapon.name} for {self.current_weapon.damage} damage.")
        target.receive_damage(self.current_weapon.damage)

    def receive_damage(self, damage):
        self.HP -= damage


class Weapon:
    def __init__(self, name, min_damage, max_damage):
        self.name = name
        self.damage = random.randint(min_damage, max_damage)


class Bear(Player):
    def __init__(self, HP=500):
        super().__init__("Bear", HP)
        self.weapons = {
            "Paw": Weapon("Paw", 10, 20),
            "Teeth": Weapon("Teeth", 20, 30)
        }

    def bear_choose_weapon(self):
        self.current_weapon = random.choice(list(self.weapons.values()))
        print(f"Bear chose {self.current_weapon.name}.")

def display_status(player, bear):
    print(f" Player HP: {player.HP}")
    print(f" Bear HP: {bear.HP}")


def main():
    system('cls')
    print("Welcome to the Bear game")

    player_name = input("Enter your name: ")
    player = Player(player_name)
    bear = Bear()

    while player.HP > 0 and bear.HP > 0:
        time.sleep(1)
        system('cls')
        print("\n" + "=" * 30)
        display_status(player, bear)
        print("\n" + "=" * 30)
        print("\nPlayer's Turn:")
        player.player_choose_weapon()
        bear.bear_choose_weapon()
        player.attack(bear)
        if bear.HP <= 0:
            print("Bear is defeated!")
            break

        print("\nBear's Turn:")
        bear.attack(player)
        if player.HP <= 0:
            print("Player is defeated!")
            break
        input("\nPress Enter to continue...")

    print("\nGame Over")
    display_status(player, bear)
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
