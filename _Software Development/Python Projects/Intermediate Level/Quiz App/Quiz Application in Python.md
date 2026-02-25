# Quiz Application in Python

The Quiz Application is a Python program that allows users to take quizzes on various topics. It includes features like multiple-choice questions, scoring, and tracking user progress. The project demonstrates concepts such as object-oriented design, file/database management, and interactive user experiences.

<h2>Key Features</h2>

- 📝 Multiple Quiz Topics: Choose from various categories (e.g., Science, History, Programming)
- ❓ Multiple-Choice Questions: Each quiz consists of multiple-choice questions with one correct answer
- 📊 Scoring System: Tracks user performance and displays the final score
- 💾 Data Storage: Store questions in JSON or a database for easy management
- 👤 User Progress Tracking: Save and retrieve user scores over multiple sessions
- 🎨 User Interface: Command-line interface (CLI), with potential for GUI using Tkinter or Flask for web-based access

<h2>Technologies Used</h2>

- Python
- Data Storage: JSON, SQLite (optional for persistence)
- User Interface: CLI (expandable to Tkinter for GUI or Flask for web)

<h2>Implementation Plan</h2>

1. Design the Quiz Structure

    - Define a ```Quiz``` class to manage the questions, scoring, and user interactions.
    - Create a ```Question``` class to represent each quiz question.

2. Store Quiz Questions

    - Use JSON or a database to store quiz questions in the following format:

```

[
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    }
]

```

4. Develop the Quiz Logic
    - Load questions from a file or database
    - Present each question and validate user input
    - Calculate and display the final score

<h2></h2>

<h3>Code Implementation (Basic CLI Version)</h3>

```

import json
import random

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def ask(self):
        print(f"\n{self.question}")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
        
        while True:
            try:
                choice = int(input("Your answer (1-4): "))
                if 1 <= choice <= len(self.options):
                    return self.options[choice - 1] == self.answer
                else:
                    print("Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

class Quiz:
    def __init__(self, filename):
        self.questions = self.load_questions(filename)
        self.score = 0

    def load_questions(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Question(q["question"], q["options"], q["answer"]) for q in data]

    def start(self):
        print("\nWelcome to the Quiz!\n")
        random.shuffle(self.questions)

        for question in self.questions:
            if question.ask():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question.answer}.\n")

        print(f"Your final score: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    quiz = Quiz('quiz_questions.json')
    quiz.start()

```

<h3>How to Use This Quiz Application</h3>

1. Prepare quiz questions:

   - Create a ```quiz_questions.json``` file and add your questions in JSON format.

2. Run the script:
   - ```python quiz_app.py```

3. Answer the questions and receive your final score.

<h3>Example Usage:</h3>

```

Welcome to the Quiz!

What is the capital of France?
1. Berlin
2. Paris
3. Madrid
4. Rome
Your answer (1-4): 2
Correct!

Which planet is known as the Red Planet?
1. Earth
2. Mars
3. Venus
4. Jupiter
Your answer (1-4): 1
Wrong! The correct answer was Mars.

Your final score: 1/2

```

<h2></h2>
<p align="center">
  <a href="https://github.com/rlangc"><b>Return to Home</b></a>
