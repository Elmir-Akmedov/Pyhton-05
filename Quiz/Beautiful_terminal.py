import time
import sys
import random

from termcolor import cprint


def custom_print(message, speed=0.1):
    for char in message:
        cprint(char, end='', flush=True)
        time.sleep(speed)
    print()


def print_title(message):
    """Prints a title with a border around it"""
    border = "=" * len(message)
    print(f"\n{border}\n{message}\n{border}\n")


def print_subtitle(message):
    """Prints a subtitle with a border around it"""
    border = "-" * len(message)
    print(f"\n{border}\n{message}\n{border}\n")


def print_success(message):
    """Prints a success message in green"""
    print(f"\033[92m{message}\033[0m")


def print_error(message):
    """Prints an error message in red"""
    print(f"\033[91m{message}\033[0m")


def print_warning(message):
    """Prints a warning message in yellow"""
    print(f"\033[93m{message}\033[0m")


def print_info(message):
    """Prints an info message in blue"""
    print(f"\033[94m{message}\033[0m")


def print_with_animation(message, color='white'):
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for char in message:
        selected_color = colors[hash(char) % len(colors)]
        cprint(char, selected_color, end='', flush=True)
        time.sleep(0.05)
    print()
    


win_art = r"""
  ________                        ________                     
 /  _____/_____    _____   ____   \_____  \___  __ ___________ 
/   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \
\    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/
 \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|   
        \/     \/      \/     \/          \/          \/       
"""

lose_art = r"""
_____.___.               __      __.__        
\__  |   | ____  __ __  /  \    /  \__| ____  
 /   |   |/  _ \|  |  \ \   \/\/   /  |/    \ 
 \____   (  <_> )  |  /  \        /|  |   |  \
 / ______|\____/|____/    \__/\  / |__|___|  /
 \/                            \/          \/ 
"""


#if __name__ == "__main__":
#    print_title("Welcome to bear game.")
#    print_subtitle("You are a warrior and you are fighting with a bear.")
#    print_subtitle("You have to kill the bear to win the game.")
#    print_success("You have won the game.")
#    print_error("You have lost the game.")
#    print_warning("You are about to die.")
#    print_info("This is an info message.")
#    print_with_animation("This is a win message", 'green')
#    print_with_animation(win_art, 'green')
#    print_with_animation("This is a lose message", 'red')
#    print_with_animation(lose_art, 'red')
#draw_box('Important Message')


def draw_box(text):
    print(f'╔{'═'*len(text)}╗')
    print(f'║{text}║')
    print(f'╚{'═'*len(text)}╝')

def draw_box2(text):
    print(f'{"-" * len(text)}')
    print(f'{text}')
    print(f'{"-" * len(text)}')
