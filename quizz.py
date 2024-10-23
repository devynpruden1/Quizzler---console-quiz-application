import json
import time
import os

class QuizApp:
    def __init__(self, filename="quiz.json"):
        self.questions = self.load_questions(filename)
        self.current_question = 0
        self.score = 0
        self.wrong_answers = []

    def load_questions(self, filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            exit()

    def display_question(self, question_data):
        question_text = question_data["question"]
        options = question_data["options"]
        print(f"\nQ{self.current_question + 1}: {question_text}")
        for i, option in enumerate(options):
            print(f"  {chr(65 + i)}. {option}")

    def get_user_answer(self):
        while True:
            user_input = input("Your answer (A, B, C, or D): ").strip().upper()
            if user_input in ['A', 'B', 'C', 'D']:
                return ord(user_input) - 65 + 1  # Convert 'A' to 1, 'B' to 2, etc.
            else:
                print("Invalid input. Please enter A, B, C, or D.")

    def run_quiz(self):
        banner = """
               
 
 ______     __  __     __     ______     ______     __         ______     ______       
/\  __ \   /\ \/\ \   /\ \   /\___  \   /\___  \   /\ \       /\  ___\   /\  == \      
\ \ \/\_\  \ \ \_\ \  \ \ \  \/_/  /__  \/_/  /__  \ \ \____  \ \  __\   \ \  __<      
 \ \___\_\  \ \_____\  \ \_\   /\_____\   /\_____\  \ \_____\  \ \_____\  \ \_\ \_\    
  \/___/_/   \/_____/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/ /_/    
                                                                                       
 ______     __  __        _____     ______     ______     __     ______                
/\  == \   /\ \_\ \      /\  __-.  /\  ___\   /\  == \   /\ \   /\__  _\               
\ \  __<   \ \____ \     \ \ \/\ \ \ \  __\   \ \  __<   \ \ \  \/_/\ \/               
 \ \_____\  \/\_____\     \ \____-  \ \_____\  \ \_____\  \ \_\    \ \_\               
  \/_____/   \/_____/      \/____/   \/_____/   \/_____/   \/_/     \/_/               
                                                                                       
     
                                               
"""

        print(banner)
        print("Welcome to the Quiz! Answer carefully.\n")

        while self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.display_question(question_data)

            user_answer = self.get_user_answer()
            correct_answer = question_data["correct_answer"]

            if user_answer == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                correct_option = chr(64 + correct_answer)  # Convert 1 to 'A', 2 to 'B', etc.
                print(f"Incorrect. The correct answer was: {correct_option}\n")
                self.wrong_answers.append(self.current_question + 1)

            self.current_question += 1

        self.show_final_score()

    def show_final_score(self):
        print("\n--- Quiz Completed! ---")
        print(f"Your Total Score: {self.score}/{len(self.questions)}")

        if self.wrong_answers:
            print("\nIncorrect Answers:")
            for question_number in self.wrong_answers:
                question_data = self.questions[question_number - 1]
                question_text = question_data["question"]
                correct_answer = question_data["options"][question_data["correct_answer"] - 1]
                print(f"Q{question_number}: {question_text}")
                print(f"Correct Answer: {correct_answer}\n")

        print("###### Let's go! W money getter lets go!!! ######")

if __name__ == "__main__":
    # Run the quiz application
    quiz = QuizApp("quizQ.json")
    quiz.run_quiz()
