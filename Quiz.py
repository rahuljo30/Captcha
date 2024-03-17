quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Jupiter", "Saturn", "Mars", "Earth"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Go", "Au", "Ag", "Gd"],
        "answer": "Au"
    },
    {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "choices": ["China", "Japan", "South Korea", "Thailand"],
        "answer": "Japan"
    }
    # Add more questions here
]
import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

# Function to display the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")  # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

    # Reset the timer
    start_timer()

# Function to check the selected answer and provide feedback
def check_answer(choice):
    global score
    global quiz_completed

    # Check if the quiz has already been completed
    if quiz_completed:
        return

    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")

    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    global quiz_completed

    current_question += 1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        if not quiz_completed:
            quiz_completed = True
            messagebox.showinfo("Quiz Completed",
                                "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
            root.quit()  # Use quit() instead of destroy() to gracefully exit the main loop

# Function to update the timer label
def update_timer():
    global timer_seconds
    timer_seconds -= 1
    timer_label.config(text="Time left: {} seconds".format(timer_seconds))
    if timer_seconds > 0:
        root.after(1000, update_timer)
    else:
        # If time is up, move to the next question
        next_question()

# Function to start the timer
def start_timer():
    global timer_seconds
    timer_seconds = 15  # Set the initial timer value to 15 seconds
    update_timer()

# Create the main window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("600x500")
style = Style(theme="flatly")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score and timer_seconds as global variables
score = 0
timer_seconds = 0
quiz_completed = False  # Flag to track whether the quiz is completed or not

# Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the timer label
timer_label = ttk.Label(
    root,
    text="Time left: {} seconds".format(timer_seconds),
    anchor="center",
    padding=10
)
timer_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()
quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Jupiter", "Saturn", "Mars", "Earth"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Go", "Au", "Ag", "Gd"],
        "answer": "Au"
    },
    {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "choices": ["China", "Japan", "South Korea", "Thailand"],
        "answer": "Japan"
    }
    # Add more questions here
]
