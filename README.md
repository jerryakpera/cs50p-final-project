# cs50p-final-project

## Quiz In A Terminal

#### Video Demo: [YouTube Video Presentation](https://youtu.be/rU3N4SdPWSU)

## Description:

The Quiz In A Terminal (QIAT henceforth) is a Python application that runs a quiz in the terminal. The quiz itself is intended to focus on syntax for programming but can be used by the user to any effect. QIAT allows the user to manage the questions to be used in the quiz using CLI commands that are parsed with argparse. These commands allow the user to add, import, view and delete question or questions. The questions used by QIAT are stored in a .csv file. The application uses OOP to manage the questions and quiz.

While the quiz is running QIAT will keep track of the questions left, your score and your current streak. Getting a question correct will remove it from the list of questions to be asked. Getting a question wrong will retain the question till you get it right.

## Purpose and explanation of each file

### project.py

The main entry file into the application. project.py imports all the other necessary modules to be discussed later and calls them depending on the system arguments the user specifies.

Here is a list of valid commands

1. **Import predefined list of questions** tuples that are in a questions.py file. Does not accept any argument

```sh
python project.py -i
```

2. **Delete questions** specified within range. Accepts any number of integers.
   If one argument is provided the question with that number is deleted.
   If 2 arguments are provided questions within least and max integers are deleted.
   If more than 2 arguments are provided questions that have the integers are deleted

```sh
python project.py -d 4 8
```

3. **View questions** specified within a range. Accepts any
   If one argument is provided the question with that number is selected.
   If 2 arguments are provided questions within least and max integers are selected.
   If more than 2 arguments are provided questions that have the integers are selected

```sh
python project.py -v 1 4 5 6
```

4. **Add question** to questions.csv file. Accepts no argument and proceeds to prompt the user for the question, answer and language of the question

```sh
python project.py -a
```

5. **Start quiz** with questions in number range provided. Accepts 2 arguments

```sh
python project.py -s 1 15
```

Below are the command that the

### Question.py

This file defines the Question class that uses static methods to manage questions for the quiz.
The Question initializes its instance by accepting a filename which is then used to store and manage the questions to be used for the quiz. This class has several helper methods for adding a list of questions, adding a single question, returning all the questions from file, filtering and returning questions by number, returning the first row of the file, returning the number of the last question returning the number of the next question to be inserted, deleting questions, initializing the file if it doesnt exist and clearing the file.

### Quiz.py

This file defines the Quiz class that creates an instance to run a quiz. The quiz class accepts a list of questions when being initialized and only asks those questions. The Quiz class uses several methods to maintain the state of a quiz, by keeping track of the score, health/lives, streak and remaining questions. Then displays this state as a header for each question allowing a user to know how many questions they have left to answer.

QIAT rewards players that have answered 3 questions correctly in a row with an extra life..

It asks each question and prompts the user to type in their answer. It captures multiline answers using a while loop to capture multiline answers and breaks out of the loop if the last line is empty.

```python
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
```

Before each question is asked the random module selects a question randomly from the list of questions.

```python
question = random.choice(quiz_questions)
```

### notice.py

File containing functions that print notices to the terminal to provide feedback for different operations

### questions_test.csv

File that is used when running the tests so as not to conflict with the main questions.csv file used to store questions and overwrite the users questions

### questions.csv

File containing comma separated list of questions. The Question class interacts with this file by deleting, adding and retrieving questions from this file.

### questions.py

Default Javascript and Python questions provided for the user to import to try out the application immediately without adding their own questions

### requirements.txt

List of modules installed for this app. This file was generated using

```python
pip freeze > requirements.txt
```

### test_project.py

File containing test functions to test three functions in the project.py file.

#### Design considerations

One of the main considerations I debated in my mind was adding multiple choice into the quiz. I went as far as implementing the multiple choice functionality but turned it off.
Grouping options for choices for each question was difficult to do in such a way that did not make it obvious what the answer was.

My first solution for the problem was to only use answers from a similar language but even then the disparity in options was so stark.

I ended up turning off the multiple choice feature all together but it can be turned off by changing the mode on line 194 to 1
