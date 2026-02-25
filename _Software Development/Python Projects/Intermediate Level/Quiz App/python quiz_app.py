
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