from time import sleep
from os import system
from rich.console import Console
from rich.progress import Progress
from rich.progress import BarColumn
from termcolor import cprint



console = Console()

# Game configuration
GAME_CONFIG = {
    "Player": {
        "HP": 100,
        "Weapons": {"Hand": None,
                     "Sword": None,
                       "Bow": None}
    },
    "Bear": {
        "HP": 500,
        "Weapons": {"Paw": None,
                     "Teeth": None}
    }
}
# Game greeting text
GREETING_TXT = (
    "Welcome to bear game.\n"
    "You are a warrior and you are fighting with a bear.\n"
    "You have to kill the bear to win the game."
)

CONTINUE_INSTRUCTION = "Press Enter to continue."

def print_with_animation(message, color='white'):
    global colors
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for char in message:
        selected_color = colors[hash(char) % len(colors)]
        cprint(char, selected_color, end='', flush=True)
        sleep(0.05)
    print()

def print_one_by_one(message, color='green'):
    for char in message:
        cprint(char, color, end='', flush=True)
        sleep(0.05)
    print()



def terminal():
    pass

def display_healt_bar(health: int, max_health: int):
    """Displays the health bar"""
    pass

def display_greeting(time: int, message: str = ''):
    message = GREETING_TXT.split('\n')
    for i in range(len(message)):
        print_one_by_one(message[i], 'yellow')
    input("Press Enter to start the game.")
    for x in range(time * 10):
        console.print(f'[blue]Game starting[/blue]{"." * (x % 10)}')
        sleep(0.1)
        system('cls' if system == 'nt' else 'cls')
    print()

display_greeting(3, GREETING_TXT)