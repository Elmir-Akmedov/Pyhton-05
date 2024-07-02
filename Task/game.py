
import random
from os import system
from time import sleep
from rich.console import Console

console = Console()
# Game configuration
GAME_CONFIG = {
    "Player": {
        "HP": 100,
        "Weapons": {"Hand": None, "Sword": None, "Bow": None}
    },
    "Bear": {
        "HP": 500,
        "Weapons": {"Paw": None, "Teeth": None}
    }
}

# Game greeting text

GREETING_TXT = (
    "[red]Welcome to bear game.\n[/red]"
    "You are a warrior and you are fighting with a bear.\n"
    "You have to kill the bear to win the game."
)

CONTINUE_INSTRACTION = "Press Enter to continue."


def display_greeting(time: int, message: str = ''):
    """Displays the greeting message and starts the game"""
    system('cls')
    console.print(message, style="bold")
    input("Press Enter to start the game.")
    for i in range(time * 10):
        system('cls')
        print(f'Game starting{"." * (i % 10)}')
        sleep(0.1)
    system('cls')


def configure_weapons():
    """Configures the damage range for each weapon"""
    player_weapons = GAME_CONFIG["Player"]["Weapons"]
    bear_weapons = GAME_CONFIG["Bear"]["Weapons"]

    player_weapons["Hand"] = random.randint(10, 20)
    player_weapons["Sword"] = random.randint(20, 50)
    player_weapons["Bow"] = random.randint(50, 80)

    bear_weapons["Paw"] = random.randint(1, 10)
    bear_weapons["Teeth"] = random.randint(10, 20)


def display_weapons(weapons: dict):
    """Displays the available weapons and their damage range"""
    print("Your weapons:\n")
    for idx, weapon in enumerate(weapons, 1):
        print(f"{idx}. {weapon} -> Damage: {weapons[weapon]}\n")
    return weapons


def choose_weapon():
    """Allows the player to choose a weapon"""
    player_weapons = GAME_CONFIG["Player"]["Weapons"]
    display_weapons(player_weapons)
    print("Choose a weapon for fight(1, 2, 3): ")
    weapon_idx = int(input(">> "))
    chosen_weapon = list(player_weapons.keys())[weapon_idx - 1]
    if chosen_weapon in player_weapons.keys():
        print(f"You have chosen {chosen_weapon}.")
        sleep(1)
        print("Now you are ready to fight with the bear.")
        print(CONTINUE_INSTRACTION, end="")
        input()
        system("cls")
    else:
        print("You have chosen wrong weapon.")
        sleep(1)
        print("Choose again.")
        choose_weapon()
    return chosen_weapon

def bear_attack():
    """Allows the bear to attack the player"""
    bear_weapons = GAME_CONFIG["Bear"]["Weapons"]
    bear_weapon = random.choice(list(bear_weapons))
    damage = bear_weapons[bear_weapon]
    print(f"Bear attacks you with {bear_weapon} - {damage} damage.")
    GAME_CONFIG["Player"]["HP"] -= damage
    sleep(1)
    display_health()
    input("Press Enter to continue.")
    system("cls")
    print("Now it's your turn.")
    sleep(1)


def attack(weapon):
    """Allows the player to attack the bear"""
    player_weapons = GAME_CONFIG["Player"]["Weapons"]
    damage = player_weapons[weapon]
    print(f"You attack the bear with {weapon} - {damage} damage.")
    GAME_CONFIG["Bear"]["HP"] -= damage
    display_health()
    input("Press Enter to continue.")
    system("cls")
    sleep(1)
    bear_attack()
    if GAME_CONFIG["Bear"]["HP"] <= 0:
        print("You have killed the bear.")
        sleep(1)
        print("You have won the game.")
    elif GAME_CONFIG["Player"]["HP"] <= 0:
        print("Bear has killed you.")
        sleep(1)
        print("You have lost the game.")
    else:
        attack(choose_weapon())


def display_health():
    """Displays the health of the player and the bear"""
    if GAME_CONFIG["Player"]["HP"] <= 0:
        GAME_CONFIG["Player"]["HP"] = 0
    if GAME_CONFIG["Bear"]["HP"] <= 0:
        GAME_CONFIG["Bear"]["HP"] = 0
    print(f"Player HP: {GAME_CONFIG['Player']['HP']}")
    sleep(1)
    print(f"Bear HP: {GAME_CONFIG['Bear']['HP']}")
    sleep(1)


def start_game():
    """Starts the game"""
    print("You have 3 weapons to kill the bear.")
    current_weapon = choose_weapon()
    attack(current_weapon)


def main():
    """Main function to control the flow of the game"""
    display_greeting(5, GREETING_TXT)
    configure_weapons()
    start_game()
    display_health()
    sleep(1)
    print("Game Over")


if __name__ == "__main__":
    main()
