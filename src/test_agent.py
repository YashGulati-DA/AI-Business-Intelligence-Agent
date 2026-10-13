from agent import ask_agent


questions = [
    "How many customers are in the database?",
    "What does the shipping policy say about delivery dates?",
    "What is the total revenue, and what does the shipping policy say?"
]

for question in questions:

    print("\n" + "=" * 60)
    print("QUESTION:", question)
    print("=" * 60)

    answer = ask_agent(question)

    print(answer)