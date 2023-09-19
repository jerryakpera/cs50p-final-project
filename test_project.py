from question import Question
from questions import questions
from project import add_question, handle_delete_question, load_questions


def test_remove_question():
    question = Question("questions_test.csv")

    question.clear_file()
    load_questions(question, questions)
    handle_delete_question(question, ["delete", "30"])

    assert question.last_question_no == 29

    question.clear_file()
    load_questions(question, questions)
    handle_delete_question(question, ["delete", "1", "10"])

    assert question.last_question_no == 21


def test_add_question():
    question = Question("questions_test.csv")
    question.clear_file()

    add_question(question, ("question", "answer", "language"))

    assert question.last_question_no == 1

    question.clear_file()

    add_question(question, ("question", "answer", "language"))
    add_question(question, ("question", "answer", "language"))

    assert question.last_question_no == 2


def test_load_questions():
    question = Question("questions_test.csv")
    question.clear_file()

    load_questions(question, questions)

    assert question.last_question_no == 30

    question.clear_file()

    load_questions(question, [])
    assert question.last_question_no == 0
