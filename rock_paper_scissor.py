import random
choices = ["rock", "paper", "scissor"]

print("""
╔══════════════════════════════════════════════════════════════════════════╗
║                       // FUTURISTIC COMBAT SIM v3.0                      ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║       ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗     ║
║       ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝     ║
║       ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗       ║
║       ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝       ║
║       ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗     ║
║        ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝     ║
║                                                                          ║
║                    >>  ROCK  •  PAPER  •  SCISSOR  <<                    ║
║                                                                          ║
║        ┌─────────────┐      ┌─────────────┐      ┌─────────────┐         ║
║        │    ROCK     │      │    PAPER    │      │  SCISSOR    │         ║
║        │  LASER-ROCK │      │  NANO-PAPER │      │ PLASMA-EDGE │         ║
║        └─────────────┘      └─────────────┘      └─────────────┘         ║                                                                          ║
║   ┌─────────────────────────────────────────────────────────────────┐    ║
║   │  [1] DEPLOY ROCK    [2] DEPLOY PAPER    [3] DEPLOY SCISSOR      │    ║
║   └─────────────────────────────────────────────────────────────────┘    ║
║                                                                          ║
║                     ░▒▓█ SYSTEM READY — CHOOSE █▓▒░                      ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
""")

while True:
    user_choice = input("\nEnter your choice (rock, paper, scissor) or 'exit' to quit: ").lower()
    print("\nProcessing your choice...\n")
    computer_choice = random.choice(choices)

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    if user_choice == "exit":
        print("Thanks for playing!")
        break

    if user_choice == "quit":
        print("Thanks for playing!")
        break

    if user_choice == "rock":
        print(f"You chose: {user_choice}")
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif user_choice == "paper":
        print(f"You chose: {user_choice}")
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif user_choice == "scissor":
        print(f"You chose: {user_choice}")
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

    if computer_choice == "rock":
        print(f"Computer chose: {computer_choice}")
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif computer_choice == "paper":
        print(f"Computer chose: {computer_choice}")
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif computer_choice == "scissor":
        print(f"Computer chose: {computer_choice}")
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

    if user_choice == computer_choice:
        print("It's a tie! Both sides are evenly matched.")
    elif (user_choice == "rock" and computer_choice == "scissor") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissor" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")