questions = [
    {
        "question": "What is the capital of India?",
        "options": ["1. Delhi", "2. Mumbai", "3. Kolkata", "4. Chennai"],
        "correct_answer": 1,
        "prize": 1000
    },
    {
        "question": "Who is the first person to climb Mount Everest?",
        "options": ["1. Sir Edmund Hillary", "2. J.R.R. Tolkien", "3. Christopher Columbus", "4. Jack Johnson"],
        "correct_answer": 1,
        "prize": 5000
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["1. Sahara", "2. Arctic", "3. Antarctica", "4. Madagascar"],
        "correct_answer": 3,
        "prize": 10000
    },
    {
        "question": "Who is the first person to step on the Moon?",
        "options": ["1. Neil Armstrong", "2. Buzz Aldrin", "3. Yuri Gagarin", "4. John Glenn"],
        "correct_answer": 1,
        "prize": 20000
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["1. Jupiter", "2. Saturn", "3. Neptune", "4. Uranus"],
        "correct_answer": 1,
        "prize": 50000
    },
    {
        "question": "What is the largest country in the world by area?",
        "options": ["1. Russia", "2. Canada", "3. China", "4. United States"],
        "correct_answer": 1,
        "prize": 200000
    },
    {
        "question": "Who is the first person to win a Nobel Prize?",
        "options": ["1. Marie Curie", "2. Albert Einstein", "3. Ada Lovelace", "4. Stephen Hawking"],
        "correct_answer": 1,
        "prize": 500000
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["1. Pacific", "2. Atlantic", "3. Indian", "4. Arctic"],
        "correct_answer": 1,
        "prize": 1000000
    },
    {
        "question": "Who is the first person to win a Nobel Prize in Physics?",
        "options": ["1. Marie Curie", "2. Albert Einstein", "3. Ada Lovelace", "4. Stephen Hawking"],
        "correct_answer": 2,
        "prize": 10000000
    }
]

def kbc(questions):
    while True:
        total_prize = 0
        for i in range(len(questions)):
            print("\n" + questions[i]["question"])
            for option in questions[i]["options"]:
                print(option)
            try:
                user_answer = int(input("Enter your answer (1-4): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
                break

            if user_answer == questions[i]["correct_answer"]:
                print("Correct answer!")
                total_prize += questions[i]["prize"]
                print(f"You have won ₹{questions[i]['prize']} so far.")
            else:
                print("Wrong answer!")
                print(f"You are taking home ₹{total_prize}.")
                break
        else:
            print(f"\nCongratulations! You answered all questions correctly and won ₹{total_prize}.")
        
        # Restart Option
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye!")
            break

# Start the game
kbc(questions)
