import sys
import notice
import argparse

from question import Question
from questions import questions
from quiz import Quiz, DIFFICULTY_MAP, MODE_MAP


def main():
    question = Question("questions.csv")

    parser = argparse.ArgumentParser(
        prog="Terminal Quizzer", description="Terminal quiz master to practice syntax"
    )

    parser.add_argument(
        "-q",
        nargs="+",
        action="extend",
        default=[],
        type=str,
        help="Manage quiz and questions",
        metavar="quiz",
    )

    args = parser.parse_args()
    flag = args.q[0]

    match (flag):
        case "load":
            load_questions(question, questions)
        case "add":
            question_input = get_question_input()

            add_question(question, question_input)
            notice.added_question()
        case "view":
            print("Viewing question(s)")
            print("--------------------")
            print(" ")
            view_questions(question, args.q)
        case "delete":
            handle_delete_question(question, args.q)
        case "start":
            start_quiz(question)


def load_questions(question, questions):
    """
    Gets users input for question, answer and topic
    Adds the question to the questions csv file

    Parameters:
        question: instance of Question class
        questions: List of tuples containing (question, answer, language)

    Returns:
        None
    """
    question.add_questions(questions)

    notice.loaded_questions()
    notice.start_quiz()


def get_question_input():
    question = input("Question: ")
    print("----------")

    answer = input("Answer: ")
    print("----------")

    language = input("Language: ")
    print("----------")

    return question, answer, language


def add_question(question, args):
    """
    Gets users input for question, answer and topic
    Adds the question to the questions csv file

    Returns:
        None
    """
    question.add_question(*args)


def convert_to_int(str):
    try:
        return int(str)
    except ValueError:
        sys.exit(f"{str} must be a number")


def get_delete_input(args):
    if len(args) == 3:
        _, start, end = args

        end_no = convert_to_int(end)
        start_no = convert_to_int(start)

        numbers_to_delete = list(range(start_no, end_no))
    elif len(args) == 2:
        _, question_no = args
        question_no = convert_to_int(question_no)

        numbers_to_delete = []
        numbers_to_delete.append(question_no)
    else:
        notice.delete_question()
        print(" ")
        notice.delete_questions()
        sys.exit()

    return numbers_to_delete


def start_quiz(question):
    languages = question.get_languages()
    languages.insert(0, "all")

    languages_str = " | ".join(languages)

    mode_str = " | ".join(MODE_MAP.keys())
    difficulty_str = " | ".join(DIFFICULTY_MAP.keys())

    # Select the language to be quizzed on
    print(f"Select programming language: ({languages_str})")
    selected_language = input("Language: ")

    if selected_language.lower() not in languages:
        print("Language not found. all languages selected")
        selected_language = "all"

    print(" ")

    # Select the quiz difficulty
    print(f"Select difficulty: ({difficulty_str})")
    selected_difficulty = input("Difficulty: ").strip().capitalize()

    if selected_difficulty not in DIFFICULTY_MAP:
        print("Difficulty not found. Medium difficulty selected")
        selected_difficulty = "Medium"

    print(" ")

    # Select the quiz mode
    print(f"Select mode: ({mode_str})")
    selected_mode = input("Mode: ").strip().capitalize()

    if selected_mode not in MODE_MAP:
        print("Mode not found. Mixed mode selected")
        selected_mode = "Mixed"

    questions = question.get_questions(selected_language)

    quiz = Quiz(questions, selected_difficulty, selected_mode)
    quiz.start()


def display_questions(questions):
    if len(questions) == 0:
        print("🪹 Nothing to display")

    for question in questions:
        print(f"{question['no']}. {question['language']}")
        print(f"Question: {question['question']}")
        print(f"Answer: {question['answer']}")
        print("____________")
        print(" ")


def get_question_no(args):
    try:
        question_no = args[1]
    except IndexError:
        return -1

    try:
        question_no = int(question_no)
    except TypeError:
        return -1

    return question_no


def view_questions(question, args):
    """
    Returns question if question_no is provided
    Otherwise returns all saved questions

    Parameters:
        question_no (str): str of the question no to display

    Returns:
        questions [question]: List of questions
    """

    question_no = get_question_no(args)

    if question_no >= 0:
        questions = question.find_question(question_no)
    else:
        questions = question.get_questions()

    display_questions(questions)
    print(" ")


def handle_delete_question(question, args):
    numbers_to_delete = get_delete_input(args)
    question.delete_questions(numbers_to_delete)


if __name__ == "__main__":
    main()
