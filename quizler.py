import random

print("-------------------------Welcome to the Quiz Game!-------------------------")

# Ask the player if they are ready to play
ready = input("Are you ready to play? (yes/no): ")

# If the player is not ready to play, exit the game
if ready.lower() != "yes":
    print("Goodbye!")
    exit()

# Define questions and answers
questions = [
    ("What is the best programming language?", "Python"),
    ("What is 2+8+9-1?", "10"),
    ("Where is Germany?", "Europe"),
    ("How many continents in the World?", "7")
]

# Initialize score and total questions
score = 0
total_questions = len(questions)

# Loop through each question
for question, answer in questions:
    # Ask the question
    user_answer = input(f"{question}: ")

    # Check if the answer is correct
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

# Calculate percentage score
score = (score / total_questions) * 100

# Display final score and passing status
print(f"Your total questions is: {total_questions}.")
print(f"Your final score is {score:.2f}%).")

# Determine pass/fail based on 75% criterion
if score >= 75:
    print("You passed the quiz.")
else:
    print("You did not pass the quiz. Try again!")
