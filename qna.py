"""Simple Q&A script."""

def main():
    questions = {
        "What is your name?": "I am QnA Bot.",
        "How are you?": "I am doing well, thank you!",
        "What is 2 + 2?": "4",
        "What is the capital of France?": "Paris",
    }

    print("Welcome to the Q&A bot! Type 'quit' to exit.\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        answer = questions.get(question, "I don't know the answer to that.")
        print(f"Bot: {answer}\n")


if __name__ == "__main__":
    main()
