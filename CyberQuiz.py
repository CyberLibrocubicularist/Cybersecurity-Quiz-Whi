# Cybersecurity Quiz Game
def run_quiz():
    # Step 1: Define the questions and answers
    questions = [
        {
            "question": "What does the acronym VPN stand for?",
            "choices": ["Virtual Private Network", "Very Private Network", "Virtual Protection Node", "Verified Protocol Network"],
            "answer": 0
        },
        {
            "question": "Which of the following is a strong password?",
            "choices": ["123456", "password", "MyP@ssw0rd!123", "qwerty"],
            "answer": 2
        },
        {
            "question": "What is the purpose of two-factor authentication?",
            "choices": [
                "To encrypt data in transit",
                "To require two forms of identification for access",
                "To prevent phishing attacks",
                "To block malware"
            ],
            "answer": 1
        },
        {
            "question": "Which of these is a common sign of phishing?",
            "choices": [
                "An email asking for personal information",
                "An email from a trusted source",
                "A secured website with HTTPS",
                "A password manager alert"
            ],
            "answer": 0
        },
        {
            "question": "What is the primary purpose of a firewall?",
            "choices": [
                "To store passwords securely",
                "To detect viruses",
                "To monitor and block unauthorized access",
                "To speed up your internet connection"
            ],
            "answer": 2
        }
    ]

    # Step 2.3: Display the questions and get the user's answers
    score = 0  # Initialize the score

    print("\nWelcome to the Cybersecurity Whiz Quiz!\n")

    for i, q in enumerate(questions):  # Loop through the questions
        print(f"Question {i + 1}: {q['question']}\n")
        for j, choice in enumerate(q['choices']):
            print(f"  {j + 1}. {choice}")  # Display each answer choice

        # Get the user's answer
        while True:
            try:
                answer = int(input("\nYour answer (1/2/3/4): ")) - 1
                if 0 <= answer < len(q['choices']):
                     break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Please enter a number between 1 and 4.")

        # Check if the answer is correct
        if answer == q['answer']:
            print("Your answer is correct, keep up the good work!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was, you'll do better next time: {q['choices'][q['answer']]}\n")

    # Display the final score
    print(f"\nYou scored {score} out of {len(questions)}!")

if __name__ == "__main__":
    run_quiz()

