import regex, random


DIFFICULTY_MAP = {
    "Easy": 7,
    "Medium": 5,
    "Hard": 3,
}

MODE_MAP = {
    "Type": 0,
    "Multiple": 1,
    "Mixed": 2,
}


class Quiz:
    """
    Quiz class to start and manage quiz session.

    Parameters:
        questions (list): List of questions with question and answer fields.
        difficulty (str): Easy, Medium or Hard difficulty.
        mode (str): Type, Multiple, or Mixed mode.

    Returns:
        quiz (Quiz): New instance of the quiz object
    """

    def __init__(self, questions, difficulty, mode) -> None:
        self.streak = 0
        self.mode = MODE_MAP[mode]
        self.lives = DIFFICULTY_MAP[difficulty]
        self.difficulty = DIFFICULTY_MAP[difficulty]

        self.questions = questions

    @property
    def questions(self):
        """
        Returns the all questions in quiz
        """
        return self._questions

    def get_random_option(self, choices, options):
        while True:
            choice = random.choice(options)

            if choice in choices:
                pass

            break

        return choice

    def get_all_multiple_choice_options(self, questions, language):
        return [
            question["answer"]
            for question in questions
            if question["language"] == language
        ]

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
        self._questions = []

        # Require the questions to be at least 4
        if len(questions) < 4:
            return "Quiz needs at least 4 questions"

        random.shuffle(questions)

        all_modes = [0, 1]

        for question in questions:
            choices = [question["answer"]]
            possible_choices = self.get_all_multiple_choice_options(
                questions, question["language"]
            )

            for _ in range(3):
                random_choice = self.get_random_option(choices, possible_choices)
                choices.append(random_choice)

                question["choices"] = choices
                if self.mode in all_modes:
                    question["mode"] = self.mode
                else:
                    question["mode"] = random.choice(all_modes)

            self._questions.append(question)

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

    def partial_match(self, users_answer, correct_answer):
        answer_regex_pattern = r"(?:" + regex.escape(users_answer) + "){e<=1}"
        answer_search = regex.findall(answer_regex_pattern, correct_answer)

        correct_answer_length = len(correct_answer)
        users_answer_length = len(users_answer)

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

        correct_answer_lines = correct_answer.split("\n")
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

    def start(self):
        """
        Method to start quiz
        Loops through each question in Quiz.questions and asks questions

        Handles correct or wrong logic
        """
        self.score = 0

        for question in self.questions:
            self.display_quiz_header()
            try:
                answer = self.ask_question(question)
            except KeyboardInterrupt:
                break

            answer_is_correct = self.check_answer(answer, question["answer"])

            if answer_is_correct:
                self.correct_answer(question["no"])
            else:
                self.incorrect_answer(question)

            if not self.game_alive:
                break
            else:
                if self.streak >= (10 - self.difficulty):
                    self.streak = 0
                    self.lives += 1

        self.end_game()

    @property
    def game_alive(self):
        """
        Returns True if user has lives
        Returns False if user has no lives
        """
        return self.lives > 0

    def correct_answer(self, question_no):
        """
        Handles correct answer logic
        Removes the question from the list of questions

        Parameters:
            question_no (str): THe no of the question the user got correct
        """
        self.score += 1
        self.streak += 1
        print("✅ Correct!")

        self._questions = [
            question for question in self.questions if question["no"] != question_no
        ]

    def incorrect_answer(self, question):
        """
        Handles login for incorrect answer
        Reduce score by 1
        Reduce lives by 1
        Resets streak

        Parameters:
            question (dict): Adds the incorrect question to the end of the questions to be asked
        """
        self.streak = 0
        self.score -= 1
        self.lives -= 1
        print(" ")
        print("🔴 Incorrect!")
        print(f"Correct answer: {question['answer']}")

        self._questions.append(question)

    @property
    def remaining_lives(self):
        """
        Return no of hearts to signify remaining lives
        """
        return "❤️" * self.lives

    def display_quiz_header(self):
        """
        Display the header for each question
        """
        print(" ")
        print("----------")
        print(f"Questions left {len(self.questions)}")
        print("Lives:", self.remaining_lives)
        print("Score:", self.score)
        print(" ")

    def ask_question(self, question):
        """
        Print question with optionsand accepts users answer

        Parameters:
            question (dict): The question to ask with question, answer and choices

        Returns:
            users_answer (str): The answer the user typed
        """
        # Ask the question
        print(f"💻 {question['language']}")
        print(question["question"])

        # If mode is type => ask for type option
        if question["mode"] == 0:
            print(" ")
            users_answer = self.get_users_typed_answer()

        # If mode is multiple choice => ask for letter
        if question["mode"] == 1:
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
