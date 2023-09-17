import re, argparse


from quiz import Quiz, DIFFICULTY_MAP, MODE_MAP
from question import Question
from questions import questions


def main():
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
        case "add":
            add_question()
            question_added()
        case "load":
            load_questions(args.q)
            questions_loaded()
        case "view":
            print("Viewing question(s)")
            print("--------------------")
            print(" ")
            view_questions(args.q)
        case "delete":
            remove_question(args.q)
        case "start":
            start_quiz()


def start_quiz():
    languages = Question.get_languages()
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

    questions = Question.get_questions(selected_language)

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


def add_question():
    """
    Gets users input for question, answer and topic
    Adds the question to the questions csv file

    Returns:
        None
    """
    question = input("Question: ")
    print("----------")

    answer = input("Answer: ")
    print("----------")

    language = input("Language: ")
    print("----------")

    Question.add_question(question, answer, language)


def load_questions(args):
    """
    Gets users input for question, answer and topic
    Adds the question to the questions csv file

    Returns:
        None
    """
    Question.add_questions(questions)


def question_added():
    print("✅")
    print("Question added successfully")

    print(" ")
    print("Run python main.py -q start to start a quiz")


def questions_loaded():
    print("✅")
    print("Question loaded successfully")

    print(" ")
    print("Run python main.py -q start to start a quiz")


def view_questions(args):
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
        questions = Question.find_question(question_no)
    else:
        questions = Question.get_questions()

    display_questions(questions)
    print(" ")


def remove_question(args):
    """
    Remove question from saved questions

    Parameters:
        question_no (str): No of question to remove

    Returns:
        None
    """

    question_no = get_question_no(args)

    if question_no >= 0:
        question = Question.find_question(question_no)

        if len(question) == 0:
            print("No question with this no")
            return

        print(f"{question[0]['no']}. {question[0]['question']}")

        confirm = input("Delete question (y | n): ")

        if confirm.lower() != "y":
            return

        Question.delete_question(question_no)

        print(" ")
        print("✅ Question deleted!")
    else:
        print("python main.py -q delete <question_no>")


if __name__ == "__main__":
    main()
