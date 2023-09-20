import regex, random
import Question


class Quiz:
    """
    Quiz class to start and manage quiz session.

    Parameters:
        questions (list): List of questions with question and answer fields.

    Returns:
        quiz (Quiz): New instance of the quiz object
    """

    def __init__(self, questions) -> None:
        self.lives = 3
        self.streak = 0
        self.questions = questions

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives):
        self._lives = lives

    @property
    def questions(self):
        """
        Returns the all questions in quiz
        """
        return self._questions

    @questions.setter
    def questions(self, questions):
        """
        Set the questions asked in the quiz.
        Appends each question to the _questions list of class

        Parameters:
            questions (list): List of questions with question and answer fields

        Returns:
            None
        """
        self._questions = questions

    def generate_choices(self, questions):
        questions_with_choices = []

        for question in questions:
            # Add the questions answer as the first choice
            choices = [question["answer"]]

            # List of all choices
            possible_choices = [question["answer"] for question in questions]

            for _ in range(3):
                random_choice = self.get_random_option(choices, possible_choices)
                choices.append(random_choice)

            question["choices"] = choices
            questions_with_choices.append(question)

        return questions_with_choices

    def get_random_option(self, choices, options):
        while True:
            choice = random.choice(options)

            if choice in choices:
                pass

            break

        return choice

    def end_game(self):
        """
        Method ran when quiz ends
        Called when lives are 0 or when user quits game

        Prints score and remark
        """
        print(" ")
        print("**************")
        print(f"Score: {self.score}")

        if self.score == len(self.questions):
            print("You are truly legendary")

        print("Game Over")
        print("**************")
        print(" ")

    def replace_quotes(self, str):
        return str.replace("'", '"')

    def partial_match(self, users_answer, correct_answer):
        u_answer = self.replace_quotes(users_answer)
        c_answer = self.replace_quotes(correct_answer)

        answer_regex_pattern = r"(?:" + regex.escape(u_answer) + "){e<=1}"
        answer_search = regex.findall(answer_regex_pattern, c_answer)

        correct_answer_length = len(c_answer)
        users_answer_length = len(u_answer)

        upper_bounds = correct_answer_length + round(correct_answer_length / 3)
        lower_bounds = correct_answer_length - round(correct_answer_length / 3)

        return (
            len(answer_search) > 0
            and lower_bounds <= users_answer_length <= upper_bounds
        )

    def check_answer(self, users_answer, correct_answer):
        if users_answer == correct_answer:
            return True

        users_answer_lines = len(users_answer)

        if users_answer_lines == 1:
            return self.partial_match(users_answer[0], correct_answer)

        correct_answer_lines = correct_answer.strip().split("\n")
        correct_answer_lines_length = len(correct_answer_lines)

        if users_answer_lines != correct_answer_lines_length:
            return False

        for i, line in enumerate(users_answer):
            trimmed_user_answer_line = line.strip()
            trimmed_correct_answer_line = correct_answer_lines[i].strip()

            if not self.partial_match(
                trimmed_user_answer_line, trimmed_correct_answer_line
            ):
                return False

        return True

    @property
    def game_alive(self):
        """
        Returns True if user has lives
        Returns False if user has no lives
        """
        return self.lives > 0

    @property
    def remaining_lives(self):
        """
        Return no of hearts to signify remaining lives
        """
        return "❤️" * self.lives

    @property
    def current_streak(self):
        """
        Return no of fire emogis to signify users streak
        """
        return "🔥" * self.streak

    def display_quiz_header(self, questions):
        """
        Display the header for each question
        """
        print(" ")
        print("----------")
        print(
            f"Questions",
            f"Score",
            f"Health",
            f"Streak",
            sep="\t\t",
        )
        print(
            f"{len(questions)} {' ' * len('questions')}",
            f"{self.score}",
            f"{self.remaining_lives}",
            f"{self.current_streak}",
            sep="\t\t",
        )
        # print(self.remaining_lives, end="\t")
        # print(self.current_streak, end="\t")
        print(" ")

    def ask_question(self, question):
        """
        Print question with optionsand accepts users answer

        Parameters:
            question (dict): The question to ask with question, answer and choices

        Returns:
            users_answer (str): The answer the user typed
        """

        # 0: Typed answers
        # 1: Multiple choice
        # [0, 1]: Mixed
        mode = 0

        # Ask the question
        print(f"💻 {question['language']}")
        print(question["question"])

        # If mode is type => ask for type option
        if mode == 0:
            print(" ")
            users_answer = self.get_users_typed_answer()

        # If mode is multiple choice => ask for letter
        if mode == 1:
            letter_keys = {"A": 0, "B": 1, "C": 2, "D": 3}
            print(" ")
            users_letter = self.get_user_choice(question["choices"])

            answer_index = letter_keys[users_letter]
            users_answer = question["choices"][answer_index]

        return users_answer

    def get_users_typed_answer(self):
        print("Type your answer. Press enter after a blank line to submit \n")
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break

        text = "\n".join(lines)

        return lines

    def get_user_choice(self, choices):
        """
        Gets users input

        Parameters:
            choices (list): List choices for user to select

        Returns:
            choice (str): A, B, C or D
        """
        choices = self.get_choices_display(choices)
        for choice in choices:
            print(choice)

        while True:
            users_selection = input("Type (A, B, C or D): ").strip().upper()

            if users_selection not in ["A", "B", "C", "D"]:
                pass
            else:
                break

        return users_selection.upper()

    def get_choices_display(self, choices):
        """
        Randomly order choices and prepends letter to choice

        Parameters:
            choices (list): List of choices

        Returns:
            choices (list): List of choices prepended with letters
        """
        option_letters = ["A", "B", "C", "D"]
        choices_display = []

        random.shuffle(choices)
        for i, choice in enumerate(choices):
            letter = option_letters[i]
            choice_display = f"{letter}. {choice}"

            choices_display.append(choice_display)

        return choices_display

    def start(self):
        """
        Method to start quiz
        Loops through each question in Quiz.questions and asks questions

        Handles correct or wrong logic
        """
        self.score = 0
        self.streak = 0

        quiz_questions = self.generate_choices(self.questions)

        while len(quiz_questions) > 0:
            question = random.choice(quiz_questions)

            self.display_quiz_header(quiz_questions)
            question_no = question["no"]

            answer = self.ask_question(question)
            answer_is_correct = self.check_answer(answer, question["answer"])

            if answer_is_correct:
                self.score += 1
                self.streak += 1
                print("✅ Correct!")

                quiz_questions = [
                    _question
                    for _question in quiz_questions
                    if _question["no"] != question_no
                ]
            else:
                self.streak = 0
                self.score -= 1
                self.lives -= 1

                print("🔴 Incorrect!")
                print("Correct Answer: ", question["answer"])

            if self.streak >= 3:
                self.streak = 0
                self.lives += 1

            if not self.game_alive:
                break

        self.end_game()
