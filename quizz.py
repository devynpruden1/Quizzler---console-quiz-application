import json
import random
import os

class QuizApp:
    def __init__(self, quiz_directory="quizzes"):
        self.quiz_directory = quiz_directory
        self.quizzes = self.load_quizzes()
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.wrong_answers = []

    def load_quizzes(self):
        quizzes = {}
        for file_name in os.listdir(self.quiz_directory):
            if file_name.endswith("_Topic_Quiz.json"):
                topic = file_name.split("_")[0]
                with open(os.path.join(self.quiz_directory, file_name), 'r') as file:
                    quizzes[topic] = json.load(file)
        return quizzes

    def display_banner(self):
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

    def choose_quiz(self):
        print("\nAvailable Quizzes:")
        topics = list(self.quizzes.keys())
        for i, topic in enumerate(topics):
            print(f"{i + 1}. {topic}")
        print(f"{len(topics) + 1}. Random (mix of all topics)")

        while True:
            try:
                choice = int(input("\nSelect a quiz by entering the number: "))
                if 1 <= choice <= len(topics):
                    return topics[choice - 1]
                elif choice == len(topics) + 1:
                    return "Random"
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def prepare_questions(self, topic, num_questions=None):
        if topic == "Random":
            all_questions = [q for questions in self.quizzes.values() for q in questions]
            max_questions = len(all_questions)
            if num_questions is None or num_questions > max_questions:
                num_questions = max_questions
            self.questions = random.sample(all_questions, num_questions)
        else:
            self.questions = self.quizzes[topic]

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
        self.display_banner()
        print("Welcome to the Quiz! Select your topic and answer carefully.")
        topic = self.choose_quiz()

        if topic == "Random":
            max_questions = sum(len(questions) for questions in self.quizzes.values())
            print(f"\nYou selected Random. There are {max_questions} total questions available.")
            while True:
                try:
                    num_questions = int(input(f"How many questions would you like (max {max_questions})? "))
                    if 1 <= num_questions <= max_questions:
                        break
                    else:
                        print("Invalid number. Please choose a number within the range.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            self.prepare_questions("Random", num_questions)
        else:
            self.prepare_questions(topic)

        print(f"\nStarting quiz on '{topic}' with {len(self.questions)} questions.\n")

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

        print("###### Thank you for playing! ######")

if __name__ == "__main__":
    # Ensure the quizzes folder exists
    quiz_directory = "quizzes"  # Place the JSON quiz files here
    if not os.path.exists(quiz_directory):
        os.makedirs(quiz_directory)
    quiz = QuizApp(quiz_directory)
    quiz.run_quiz()
