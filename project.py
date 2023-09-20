import sys
import notice
import argparse

from Quiz import Quiz
from Question import Question
from questions import questions


def main():
    question = Question("questions.csv")
    quiz_parser(question)


def quiz_parser(question):
    parser = argparse.ArgumentParser(
        prog="TerminalTrivia",
        description="Trivia for practicing and mastering basic programming syntax",
        epilog="Run: 'python project.py -s' to get started",
    )

    parser.add_argument(
        "-i",
        "--import_questions",
        action="store_true",
        help="Import list of questions",
    )

    parser.add_argument(
        "-v",
        "--view",
        type=int,
        nargs="*",
        metavar="numbers to view",
        dest="view_question_nos",
        help="View question(s). Use 0 to view all",
    )

    parser.add_argument(
        "-d",
        "--delete",
        type=int,
        nargs="*",
        dest="delete_question_nos",
        metavar="numbers",
        help="Delete question(s). Use 0 to delete all",
    )

    parser.add_argument(
        "-s",
        "--start",
        type=int,
        nargs=2,
        metavar="(start, end)",
        dest="quiz_numbers",
        help="Question numbers for quiz. Use 0 for all",
    )

    parser.add_argument("-a", "--add", help="Add new question", action="store_true")
    parser.add_argument(
        "-c", "--clear", help="Clear all questions from file", action="store_true"
    )

    args = parser.parse_args()

    if args.quiz_numbers:
        quiz_numbers = get_list_of_numbers(args.quiz_numbers)
        quiz_questions = question.filter_questions_by_no(quiz_numbers)

        quiz = Quiz(quiz_questions)

        try:
            quiz.start()
        except KeyboardInterrupt:
            quiz.end_game()

        sys.exit()

    if args.clear:
        question.clear_file()

        notice.cleared_questions()

        sys.exit()

    if args.add:
        try:
            question_input = get_question_input()
        except KeyboardInterrupt:
            print("")
            print("")
            sys.exit("🔴 Cancelled")

        add_question(question, question_input)

        notice.added_question()

        sys.exit()

    if args.import_questions:
        load_questions(question, questions)
        sys.exit()

    if args.view_question_nos:
        # Get the numbers of the questions to view while removing duplicates
        filter_question_numbers = get_list_of_numbers(args.view_question_nos)
        questions_to_display = question.filter_questions_by_no(filter_question_numbers)

        display_questions(questions_to_display)
        sys.exit()

    if args.delete_question_nos:
        # Get the numbers of the questions to delete while removing duplicates
        filter_question_numbers = get_list_of_numbers(args.delete_question_nos)
        question.delete_questions(filter_question_numbers)

        notice.question_deleted()
        sys.exit()

    parser.print_help()


def get_list_of_numbers(numbers_list):
    filter_question_numbers = list(set(numbers_list))
    filter_question_numbers = sorted(filter_question_numbers)

    if len(filter_question_numbers) == 2:
        start, end = filter_question_numbers
        filter_question_numbers = list(range(start, end + 1))

    return filter_question_numbers


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


def get_question_input():
    question = input("Type the question: ")
    print(" ")

    answer = input("Type the answer: ")
    print(" ")

    language = input("Language: ")
    print(" ")

    return question, answer, language


def add_question(question, args):
    """
    Gets users input for question, answer and topic
    Adds the question to the questions csv file

    Returns:
        None
    """
    question.add_question(*args)


def display_questions(questions):
    if len(questions) == 0:
        print("🪹 Nothing to display")

    for question in questions:
        print(" ")
        print(f"Question {question['no']} ({question['language']})")
        print(question["question"])
        print(" ")
        print("Answer")
        print(question["answer"])
        print(" ")
        print(" ")
        print("----------")
        print(" ")


if __name__ == "__main__":
    main()
