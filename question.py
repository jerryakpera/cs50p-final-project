import csv


class Question:
    """Documentation for the Question class."""

    def __init__(self, file_name) -> None:
        self.questions_fieldnames = [
            "no",
            "question",
            "answer",
            "language",
        ]
        self.file_name = file_name
        self.initialize_file()

    def add_questions(self, questions):
        """
        Adds questions to self.file_name csv

        Parameters:
            questions: (list of (str, str))

        Returns:
            None
        """
        for ques in questions:
            self.add_question(*ques)

    def add_question(self, question, answer, language="python"):
        """
        Adds a question to self.file_name csv

        Parameters:
            question (str): A string containing the question
            answer (str): The answer to the question

        Returns:
            None
        """
        last_no = self.next_question_no

        new_question = {
            "no": last_no,
            "question": question,
            "answer": answer,
            "language": language,
        }

        headers = self.first_row

        with open(self.file_name, "a", newline="") as questions_file:
            writer = csv.DictWriter(
                questions_file, fieldnames=self.questions_fieldnames
            )

            if not headers:
                writer.writeheader()

            writer.writerow(new_question)

    def get_questions(self):
        """
        Get all questions from csv file

        Parameters:

        Returns:
            questions (list of dicts): List of dicts with questions and answers
        """
        questions = []

        with open(self.file_name, newline="") as questions_file:
            file_reader = csv.DictReader(questions_file)

            for question_row in file_reader:
                questions.append(question_row)

        return questions

    def filter_questions_by_no(self, question_nos):
        """
        Finds and returns a question from csv file

        Parameter:
            no (str or int): The unique identifier of the question

        Returns:
            question (dict): Dict containing no, question and answer fields
        """
        questions = self.get_questions()

        if len(question_nos) == 1 and question_nos[0] == 0:
            return questions

        return [ques for ques in questions if int(ques.get("no")) in question_nos]

    @property
    def first_row(self):
        """
        Retrieve the first row of the csv

        Returns:
            field_names (list): List of items in first row
        """
        with open(self.file_name, newline="") as questions_file:
            file_reader = csv.DictReader(questions_file)
            return file_reader.fieldnames

    @property
    def last_question_no(self):
        """
        Retrieve the no of the last question

        Returns:
            no (str or int): Number for the next question
        """
        questions = self.get_questions()

        try:
            return int(questions[-1]["no"])
        except IndexError:
            return 0

    @property
    def next_question_no(self):
        """
        Retrieve the index for the next question

        Returns:
            no (str or int): Number for the next question
        """
        return self.last_question_no + 1

    def delete_questions(self, numbers):
        """
        Remove question from csv file

        Parameters:
            row_no (str or int): Value of question id in csv file

        Returns:
            None
        """
        questions = self.get_questions()

        filtered_questions = [
            question for question in questions if int(question["no"]) not in numbers
        ]

        with open(self.file_name, "w", newline="") as questions_file:
            writer = csv.DictWriter(
                questions_file, fieldnames=self.questions_fieldnames
            )
            writer.writeheader()

            for i, question in enumerate(filtered_questions):
                question["no"] = i + 1
                writer.writerow(question)

    def initialize_file(self):
        try:
            with open(self.file_name, newline=""):
                ...
        except FileNotFoundError:
            with open(self.file_name, "w"):
                ...

    def clear_file(self):
        # opening the file with w+ mode truncates the file
        f = open(self.file_name, "w+")
        f.close()
