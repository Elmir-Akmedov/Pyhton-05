from time import sleep
from random import choice
from os import system
from rich.console import Console
from rich.progress import Progress, BarColumn


# Initialize Rich console
console = Console()

# Game configuration
GAME_CONFIG = {
    "Player": {"HP": 100, "Weapons": {"Hand": None, "Sword": None, "Bow": None}},
    "Bear": {"HP": 500, "Weapons": {"Paw": None, "Teeth": None}},
}

GREETING_TXT = (
    "Welcome to bear game.\n"
    "You are a warrior and you are fighting with a bear.\n"
    "You have to kill the bear to win the game."
)

CONTINUE_INSTRUCTION = "Press Enter to continue."


def print_with_animation(message, speed=0.05):
    """Prints message with each character in random color"""
    for char in message:
        color = choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
        console.print(char, style=color, end='', highlight=False)
        sleep(speed)
    print()


def display_greeting(time: int, message: str = ''):
    """Displays the greeting message and starts the game"""
    system('cls' if system == 'nt' else 'cls')
    print_with_animation(message)
    print_with_animation(CONTINUE_INSTRUCTION)
    input()
    for _ in range(time * 10):
        system('cls' if system == 'nt' else 'cls')
        console.print(f'Game starting{"." * (_ % 10)}', style="bold yellow")
        sleep(0.1)
    system('cls' if system == 'nt' else 'cls')


def configure_weapons():
    """Configures the damage range for each weapon"""
    player_weapons = GAME_CONFIG["Player"]["Weapons"]
    bear_weapons = GAME_CONFIG["Bear"]["Weapons"]

    player_weapons["Hand"] = choice(range(10, 21))
    player_weapons["Sword"] = choice(range(20, 51))
    player_weapons["Bow"] = choice(range(50, 81))

    bear_weapons["Paw"] = choice(range(1, 11))
    bear_weapons["Teeth"] = choice(range(10, 21))


def display_weapons(weapons: dict):
    """Displays the available weapons and their damage range"""
    console.print("[yellow]Your weapons:[/yellow]")
    for idx, (weapon, damage) in enumerate(weapons.items(), 1):
        console.print(f"[cyan]{idx}. {weapon} -> Damage: {damage}[/cyan]")
    return weapons


def choose_weapon():
    """Allows the player to choose a weapon"""
    player_weapons = GAME_CONFIG["Player"]["Weapons"]
    display_weapons(player_weapons)
    console.print("[cyan]Choose a weapon for fight (1, 2, 3): [/cyan]", end="")
    weapon_idx = int(input(">> "))
    chosen_weapon = list(player_weapons.keys())[weapon_idx - 1]
    if chosen_weapon in player_weapons.keys():
        print_with_animation(f"You have chosen [yellow]{chosen_weapon}[/yellow].")
        sleep(1)
        print_with_animation("Now you are ready to fight with the bear.")
        print_with_animation(CONTINUE_INSTRUCTION)
        input()
        system("cls" if system == 'nt' else 'cls')
    else:
        print_with_animation("You have chosen wrong weapon.")
        sleep(1)
        print_with_animation("Choose again.")
        choose_weapon()
    return chosen_weapon


def bear_attack():
    """Allows the bear to attack the player"""
    bear_weapons = GAME_CONFIG["Bear"]["Weapons"]
    bear_weapon = choice(list(bear_weapons))
    damage = bear_weapons[bear_weapon]
    print_with_animation(f"Bear attacks you with [red]{bear_weapon}[/red] - [red]{damage}[/red] damage.")
    GAME_CONFIG["Player"]["HP"] -= damage
    sleep(1)
    display_health()
    input(CONTINUE_INSTRUCTION)
    system("cls" if system == 'nt' else 'cls')
    print_with_animation("Now it's your turn.")
    sleep(1)


def attack(weapon):
    """Allows the player to attack the bear"""
    player_weapons = GAME_CONFIG["Player"]["Weapons"]
    damage = player_weapons[weapon]
    print_with_animation(f"You attack the bear with [yellow]{weapon}[/yellow] - [yellow]{damage}[/yellow] damage.")
    GAME_CONFIG["Bear"]["HP"] -= damage
    display_health()
    input(CONTINUE_INSTRUCTION)
    system("cls" if system == 'nt' else 'cls')
    sleep(1)
    bear_attack()
    if GAME_CONFIG["Bear"]["HP"] <= 0:
        print_with_animation("[green]You have killed the bear.[/green]")
        sleep(1)
        print_with_animation("[green]You have won the game.[/green]")
    elif GAME_CONFIG["Player"]["HP"] <= 0:
        print_with_animation("[red]Bear has killed you.[/red]")
        sleep(1)
        print_with_animation("[red]You have lost the game.[/red]")
    else:
        attack(choose_weapon())


def display_health():
    """Displays the health of the player and the bear"""
    if GAME_CONFIG["Player"]["HP"] <= 0:
        GAME_CONFIG["Player"]["HP"] = 0
    if GAME_CONFIG["Bear"]["HP"] <= 0:
        GAME_CONFIG["Bear"]["HP"] = 0
    
    with Progress(transient=True) as progress:
        player_progress = progress.add_task("[cyan]Player Health", total=100, start=100)
        bear_progress = progress.add_task("[red]Bear Health", total=500, start=500)
        console.print(progress, BarColumn(), end="")

    console.print(f"\nPlayer HP: [cyan]{GAME_CONFIG['Player']['HP']}[/cyan]")
    console.print(f"Bear HP: [red]{GAME_CONFIG['Bear']['HP']}[/red]")


def start_game():
    """Starts the game"""
    print_with_animation("You have 3 weapons to kill the bear.")
    current_weapon = choose_weapon()
    attack(current_weapon)


def main():
    """Main function to control the flow of the game"""
    display_greeting(5, GREETING_TXT)
    configure_weapons()
    start_game()
    display_health()
    sleep(1)
    print_with_animation("[red]Game Over[/red]")


if __name__ == "__main__":
    main()
