![Quiz Banner](banner.png)

The Quizzler is a Python-based command-line quiz application that loads questions from a JSON file, asks users multiple-choice questions, and keeps track of their scores. The app offers feedback on correct and incorrect answers and displays the final score with a summary of missed questions at the end.

Features:
Loads quiz questions from a JSON file.
Asks multiple-choice questions (supports options A, B, C, D).
Provides immediate feedback for correct/incorrect answers.
Keeps track of the total score and shows a detailed summary at the end.
Displays a banner with a motivational message at the start and finish.
Installation
Prerequisites
Python 3.x installed. You can download Python here.

Setup:
Clone or download the repository containing the Quiz application.

Ensure your JSON file is named quizQ.json and placed in the same directory as your Python script.

How to Run the Quiz:
Open a terminal or command prompt.
Navigate to the directory where the quizz script is located.
type: python quiz.py


JSON File Example:
Here is an example quizQ.json file:

[
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Shark", "Giraffe"],
        "correct_answer": 2
    },
    {
        "question": "How many continents are there?",
        "options": ["5", "6", "7", "8"],
        "correct_answer": 3
    }
]

Feel free to fork the project and submit pull requests to improve the code or add new features.

Enjoy the quiz and show off your knowledge! 🎉