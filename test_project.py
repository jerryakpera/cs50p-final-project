from Question import Question
from questions import questions
from project import get_list_of_numbers, add_question, load_questions


def get_list_of_numbers():
    assert get_list_of_numbers([1, 4]) == [1, 2, 3, 4]
    assert get_list_of_numbers([1, 2, 3, 6]) == [1, 2, 3, 6]
    assert get_list_of_numbers([13]) == [13]


def test_add_question():
    test_question = Question("questions_test.csv")
    test_question.clear_file()

    assert test_question.last_question_no == 0

    test_question.add_question(
        "Is this a question?", "How am I supposed to answer that?", "life"
    )

    assert test_question.last_question_no == 1

    test_question.clear_file()

    assert test_question.last_question_no == 0

    for question in questions:
        test_question.add_question(*question)

    assert test_question.last_question_no == 28


def test_load_questions():
    test_question = Question("questions_test.csv")
    test_question.clear_file()

    assert test_question.last_question_no == 0

    load_questions(test_question, questions)

    assert test_question.last_question_no == 28
