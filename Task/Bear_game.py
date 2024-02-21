from os import system
from time import sleep
import random



def greeting():
    print("Welcome to Bear Game!!!")
    sleep(1.5)
    print("You are a warrior and you are fighting with a bear.")
    sleep(1.5)
    print("You have to kill the bear to win the game.")
    sleep(1.5)

def start_game():
    weapons_damage_configuration()
    print("You have 3 weapons to kill the bear.")
    current_weapon = choose_weapon()
    attack(current_weapon)


def attack(weapon, player_name="Player"):
    damage = bear_game[player_name]["Weapons"][weapon]
    print(f"You attack the bear with {weapon} - {damage} damage.")
    bear_game["Bear"]["HP"] -= damage
    sleep(1)
    display_healt()
    input("Press Enter to continue.")
    system("cls")
    print("Bear is attacking you.")
    sleep(1)
    bear_attack()
    if bear_game["Bear"]["HP"] <= 0:
        print("You have killed the bear.")
        sleep(1)
        print("You have won the game.")
    elif bear_game["Player"]["HP"] <= 0:
        print("Bear has killed you.")
        sleep(1)
        print("You have lost the game.")
    else:
        attack(choose_weapon())
    
def bear_attack():
    damage = random.choice(list(bear_game["Bear"]["Weapons"].values()))
    print(f"Bear attacks you with {damage} damage.")
    bear_game["Player"]["HP"] -= damage
    sleep(1)
    display_healt()
    input("Press Enter to continue.")
    system("cls")
    print("Now it's your turn.")
    sleep(1)

def main():
    start_game()

def weapons_damage_configuration():
    for weapon in bear_game["Player"]["Weapons"]:
        if weapon == "Hand":
            bear_game["Player"]["Weapons"][weapon] = random.randint(10, 20)
        elif weapon == "Sword":
            bear_game["Player"]["Weapons"][weapon] = random.randint(20, 50)
        elif weapon == "Bow":
            bear_game["Player"]["Weapons"][weapon] = random.randint(50, 80)
    
    for weapon in bear_game["Bear"]["Weapons"]:
        if weapon == "Paw":
            bear_game["Bear"]["Weapons"][weapon] = random.randint(1, 10)
        elif weapon == "Teeth":
            bear_game["Bear"]["Weapons"][weapon] = random.randint(10, 20)

def weapons(weapons: dict):
    print("Your weapons:")
    for idx, weapon in enumerate(weapons, 1):
        print(f"{idx}. {weapon}")
        sleep(1)
    return weapons

def choose_weapon():
    player_weapons = bear_game["Player"]["Weapons"]
    weapons(player_weapons)
    weapon_idx = int(input("Choose a weapon for fight(1, 2, 3): "))
    choosen_weapon = list(player_weapons.keys())[weapon_idx - 1]
    if choosen_weapon in player_weapons.keys():
        print(f"You have chosen {choosen_weapon}.")
        sleep(1)
        print("Now you are ready to fight with the bear.")
        input("Press Enter to continue.")
        system("cls")
    else:
        print("You have chosen wrong weapon.")
        sleep(1)
        print("Choose again.")
        choose_weapon()
    return choosen_weapon
    
def terminal():
    system("cls")
    greeting()

def display_healt():
    if bear_game["Player"]["HP"] <= 0:
        bear_game["Player"]["HP"] = 0
    if bear_game["Bear"]["HP"] <= 0:
        bear_game["Bear"]["HP"] = 0
    print(f"Player : {bear_game['Player']['HP']}")
    sleep(1)
    print(f"Bear : {bear_game['Bear']['HP']}")
    sleep(1)

bear_game = {
    "Player": {
        "HP": 100,
        "Weapons": {"Hand": None,
                       "Sword": None,
                         "Bow": None}
    },
    "Bear": {
        "HP": 500,
        "Weapons": {"Paw": None,
                    "Teeth": None,}
    }
}

if __name__ == "__main__":
    terminal()
    main()
    display_healt()
    sleep(1)
    print("Game Over")
    