import tkinter as tk
from tkinter import messagebox

# Questions for the game
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        "correct_answer": 0,
        "prize": 1000
    },
    {
        "question": "Who is the first person to climb Mount Everest?",
        "options": ["Sir Edmund Hillary", "J.R.R. Tolkien", "Christopher Columbus", "Jack Johnson"],
        "correct_answer": 0,
        "prize": 5000
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["Sahara", "Arctic", "Antarctica", "Madagascar"],
        "correct_answer": 2,
        "prize": 10000
    },
        {
        "question": "Who is the first person to step on the Moon?",
        "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn"],
        "correct_answer": 0,
        "prize": 20000
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Jupiter", "Saturn", "Neptune", "Uranus"],
        "correct_answer": 0,
        "prize": 50000
    },
    {
        "question": "What is the largest country in the world by area?",
        "options": ["Russia", "Canada", "China", "United States"],
        "correct_answer": 0,
        "prize": 200000
    },
    {
        "question": "Who is the first person to win a Nobel Prize?",
        "options": ["Marie Curie", "Albert Einstein", "Ada Lovelace", "Stephen Hawking"],
        "correct_answer": 0,
        "prize": 500000
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["Pacific", "Atlantic", "Indian", "Arctic"],
        "correct_answer": 0,
        "prize": 1000000
    },
    {
        "question": "Who is the first person to win a Nobel Prize in Physics?",
        "options": ["Marie Curie", "Albert Einstein", "Ada Lovelace", "Stephen Hawking"],
        "correct_answer": 1,
        "prize": 10000000
    }

]

# Variables to keep track of the game
current_question = 0
total_prize = 0

# Function to display the next question
def next_question():
    global current_question, total_prize

    if current_question < len(questions):
        question = questions[current_question]
        question_label.config(text=question["question"])
        for i, option in enumerate(question["options"]):
            buttons[i].config(text=option, command=lambda opt=i: check_answer(opt))
    else:
        messagebox.showinfo("Game Over", f"Congratulations! You won ₹{total_prize}!")
        root.destroy()

# Function to check the answer
def check_answer(selected_option):
    global current_question, total_prize

    question = questions[current_question]
    if selected_option == question["correct_answer"]:
        total_prize += question["prize"]
        messagebox.showinfo("Correct!", f"Correct answer! You've won ₹{question['prize']} so far.")
        current_question += 1
        next_question()
    else:
        messagebox.showinfo("Wrong Answer", f"Wrong answer! You take home ₹{total_prize}.")
        root.destroy()

# Function to start the game
def start_game():
    start_button.pack_forget()
    next_question()

# Create the main Tkinter window
root = tk.Tk()
root.title("KBC Game")
root.geometry("500x300")

# Welcome label
welcome_label = tk.Label(root, text="Welcome to KBC!", font=("Arial", 18))
welcome_label.pack(pady=10)

# Start button
start_button = tk.Button(root, text="Play KBC", font=("Arial", 14), command=start_game)
start_button.pack(pady=20)

# Question label
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
question_label.pack(pady=20)

# Option buttons
buttons = [tk.Button(root, text="", font=("Arial", 12), width=30) for _ in range(4)]
for button in buttons:
    button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
