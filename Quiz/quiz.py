import time
import random
import requests
from colorama import Fore, Style  # Importing Colorama for color formatting
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def custom_print(message, speed=0.1):
    """Prints each character of a message with a delay."""
    for char in message:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()


def print_title(message):
    """Prints a title with a border around it."""
    border = "=" * len(message)
    print(f"\n{Fore.YELLOW}{border}\n{message}\n{border}\n")


def print_subtitle(message):
    """Prints a subtitle with a border around it."""
    border = "-" * len(message)
    print(f"\n{Fore.YELLOW}{border}\n{message}\n{border}\n")


def print_success(message):
    """Prints a success message in green."""
    print(f"{Fore.GREEN}{message}")


def print_error(message):
    """Prints an error message in red."""
    print(f"{Fore.RED}{message}")


def print_warning(message):
    """Prints a warning message in yellow."""
    print(f"{Fore.YELLOW}{message}")


def print_info(message):
    """Prints an info message in blue."""
    print(f"{Fore.BLUE}{message}")


def print_with_animation(message):
    """Prints a message with each character animated in different colors."""
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    for char in message:
        selected_color = random.choice(colors)
        print(selected_color + char, end='', flush=True)
        time.sleep(0.05)
    print()


def interact_with_chatgpt(prompt):
    """Interacts with ChatGPT to get a response."""
    driver = webdriver.Chrome()  # You can replace this with any other webdriver
    driver.get("https://chat.openai.com/")  # Replace with the actual URL

    # Find the input field and send the prompt
    input_field = driver.find_element_by_id("prompt-textarea")  # Replace with the actual element ID
    input_field.send_keys(prompt)
    input_field.send_keys(Keys.RETURN)

    # Wait for ChatGPT response
    response_element = driver.find_element_by_id("p-4 overflow-y-auto")  # Replace with the actual element ID
    response = response_element.text

    driver.quit()
    return response


def fetch_questions_from_chatgpt():
    """Fetches questions from ChatGPT."""
    prompt = "Generate a quiz with 10 questions and answers.\n"
    return interact_with_chatgpt(prompt)


def fetch_questions_from_web():
    """Fetches questions from a web page."""
    # Example: Fetch questions from a webpage using Selenium
    driver = webdriver.Chrome()
    driver.get("https://example.com/quiz")

    questions = []
    question_elements = driver.find_elements_by_class_name("question")
    for q_element in question_elements:
        text = q_element.text
        choices = []
        choice_elements = q_element.find_elements_by_class_name("choice")
        for i, choice_element in enumerate(choice_elements):
            is_correct = i == 0  # Assuming first choice is correct
            choices.append({"text": choice_element.text, "is_correct": is_correct})
        questions.append({"text": text, "choices": choices})

    driver.quit()
    return questions


def customize_quiz():
    """Customizes the quiz based on user preferences."""
    num_questions = int(input(f"{Fore.YELLOW}Enter the number of questions for the quiz: "))
    difficulty_level = input(f"{Fore.YELLOW}Enter the difficulty level (easy, medium, hard): ").lower()

    # Customize the quiz based on user preferences
    if difficulty_level == "easy":
        # Fetch easy questions from ChatGPT or any other source
        questions = fetch_questions_from_chatgpt()
    elif difficulty_level == "medium":
        # Fetch medium questions
        questions = fetch_questions_from_web()
    elif difficulty_level == "hard":
        # Fetch hard questions
        questions = fetch_questions_from_web()
    else:
        print_warning("Invalid difficulty level. Quiz will proceed with default settings.")
        questions = fetch_questions_from_web()

    return questions[:num_questions]  # Return the specified number of questions


def create_leaderboard(score):
    """Creates or updates the leaderboard with the given score."""
    # Load existing leaderboard data
    try:
        with open("leaderboard.txt", "r") as file:
            leaderboard_data = file.readlines()
    except FileNotFoundError:
        leaderboard_data = []

    # Append new score to the leaderboard data
    leaderboard_data.append(f"Score: {score}\n")

    # Sort the leaderboard data based on scores
    leaderboard_data.sort(key=lambda x: int(x.split(": ")[1]), reverse=True)

    # Write the updated leaderboard data to the file
    with open("leaderboard.txt", "w") as file:
        file.writelines(leaderboard_data)


def display_leaderboard():
    """Displays the leaderboard."""
    try:
        with open("leaderboard.txt", "r") as file:
            leaderboard_data = file.read()
        print("Leaderboard:")
        print(leaderboard_data)
    except FileNotFoundError:
        print("Leaderboard is empty.")


def save_quiz_progress(current_question_index, unanswered_questions):
    """Saves the current quiz progress."""
    with open("quiz_progress.txt", "w") as file:
        file.write(f"{current_question_index}\n")
        for question in unanswered_questions:
            file.write(f"{question['text']}\n")
            for choice in question['choices']:
                file.write(f"{choice['text']},{choice['is_correct']}\n")
            file.write("\n")


def load_quiz_progress():
    """Loads the saved quiz progress."""
    current_question_index = 0
    unanswered_questions = []

    try:
        with open("quiz_progress.txt", "r") as file:
            lines = file.readlines()
            current_question_index = int(lines[0])
            question_lines = lines[1:]
            i = 0
            while i < len(question_lines):
                text = question_lines[i].strip()
                choices = []
                i += 1
                while i < len(question_lines) and question_lines[i].strip():
                    choice_text, is_correct = question_lines[i].strip().split(",")
                    choices.append({"text": choice_text, "is_correct": is_correct})
                    i += 1
                unanswered_questions.append({"text": text, "choices": choices})
    except FileNotFoundError:
        pass

    return current_question_index, unanswered_questions


def main():
    print_title("Welcome to the Quiz!")

    # Customize the quiz
    questions = customize_quiz()

    # Quiz logic goes here
    total_questions = len(questions)
    correct_answers = 0

    for i, question in enumerate(questions, start=1):
        print_subtitle(f"Question {i}/{total_questions}")
        print(f"{question['text']}")
        for choice in question["choices"]:
            print(f"{Fore.CYAN}{choice['text']}")
        user_answer = input(f"{Fore.YELLOW}Your answer: ").strip().lower()
        correct_choice = question["choices"][0]["text"].lower()
        if user_answer == correct_choice:
            print_success("Correct!")
            correct_answers += 1
        else:
            print_error("Incorrect!")
            print_info(f"Correct answer: {correct_choice}")

    print_title("Quiz Results")
    print_info(f"Your score is: {correct_answers}/{total_questions}")

    # Save quiz progress
    save_quiz_progress(0, questions)

    # Create or update leaderboard
    create_leaderboard(correct_answers)

    # Display leaderboard
    display_leaderboard()


if __name__ == "__main__":
    main()
