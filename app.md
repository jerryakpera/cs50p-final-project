## Features

### Question

[x] User can CRUD question
[x] User can view all questions
[x] User can reset their scores
question {
no: int;
question: str;
answer: str;
attempts: int;
correct: int;
wrong: int;
}

### Quiz

- User can generate and save quiz - form a quiz from a group of questions (all, topic, or scores) and export to file that user specifies
- User can start quiz - form a quiz from a group of questions (all, topic, or scores) and start quiz
- Quiz has different modes - multiple choice (requires at least 4 questions), type in the answer or both
- Quiz keeps track of total score
- Quiz keeps track of score (1 or 0) for each question
- Quiz displays users score after completion
  quiz: [
  {
  question,
  options,
  score: 1 | 0
  }
  ]
