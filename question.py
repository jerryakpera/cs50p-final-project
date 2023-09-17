import csv


class Question:
    """Documentation for the Question class."""

    questions_fieldnames = [
        "no",
        "question",
        "answer",
        "language",
    ]
    file_name = "questions.csv"

    @classmethod
    def set_file_name(cls, file_name):
        """
        Change the file name to store questions

        Parameters:
            file_name (str): The name of the file to store questions
        """
        cls.file_name = file_name

    @classmethod
    def add_questions(cls, questions):
        """
        Adds questions to cls.file_name csv

        Parameters:
            questions: (list of (str, str))

        Returns:
            None
        """
        for ques in questions:
            cls.add_question(*ques)

    @classmethod
    def add_question(cls, question, answer, language="python"):
        """
        Adds a question to cls.file_name csv

        Parameters:
            question (str): A string containing the question
            answer (str): The answer to the question

        Returns:
            None
        """
        last_no = cls.get_last_question_no()

        new_question = {
            "no": last_no,
            "question": question,
            "answer": answer,
            "language": language,
        }

        headers = cls.get_first_row()

        with open(cls.file_name, "a", newline="") as questions_file:
            writer = csv.DictWriter(questions_file, fieldnames=cls.questions_fieldnames)

            if not headers:
                writer.writeheader()

            writer.writerow(new_question)

    @classmethod
    def get_questions(cls, language="all"):
        """
        Get all/language questions from csv file

        Parameters:
            language (str): Language to use to filter out questions

        Returns:
            questions (list of dicts): List of dicts with questions and answers
        """
        questions = []

        with open(cls.file_name, newline="") as questions_file:
            file_reader = csv.DictReader(questions_file)

            for question_row in file_reader:
                if language == "all":
                    questions.append(question_row)
                    pass

                if question_row["language"] == language:
                    questions.append(question_row)
                    pass

        return questions

    @classmethod
    def find_question(cls, no):
        """
        Finds and returns a question from csv file

        Parameter:
            no (str or int): The unique identifier of the question

        Returns:
            question (dict): Dict containing no, question and answer fields
        """
        questions = cls.get_questions()

        return [ques for ques in questions if ques.get("no") == str(no)]

    @classmethod
    def get_first_row(cls):
        """
        Retrieve the first row of the csv

        Returns:
            field_names (list): List of items in first row
        """
        with open(cls.file_name, newline="") as questions_file:
            file_reader = csv.DictReader(questions_file)
            return file_reader.fieldnames

    @classmethod
    def get_last_question_no(cls):
        """
        Retrieve the no of the last question

        Returns:
            no (str or int): Number for the next question
        """
        questions = cls.get_questions()

        try:
            return int(questions[-1]["no"]) + 1
        except IndexError:
            return 1

    @classmethod
    def delete_question(cls, row_no):
        """
        Remove question from csv file

        Parameters:
            row_no (str or int): Value of question id in csv file

        Returns:
            None
        """
        questions = cls.get_questions()
        filtered_questions = [
            question for question in questions if question["no"] != str(row_no)
        ]

        with open(cls.file_name, "w", newline="") as questions_file:
            writer = csv.DictWriter(questions_file, fieldnames=cls.questions_fieldnames)
            writer.writeheader()

            for i, question in enumerate(filtered_questions):
                question["no"] = i + 1
                writer.writerow(question)

    @classmethod
    def get_languages(cls):
        languages = []

        for question in cls.get_questions():
            language = question["language"]

            if language not in languages:
                languages.append(language)

        return languages
