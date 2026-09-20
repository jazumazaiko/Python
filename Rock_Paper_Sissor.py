import random

def rps():
    print("""
██████╗   ██████╗   ██████╗ ██╗  ██╗
██╔══██╗ ██╔═══██╗ ██╔════╝ ██║ ██╔╝
██████╔╝ ██║   ██║ ██║      █████╔╝ 
██╔══██╗ ██║   ██║ ██║      ██╔═██╗ 
██║  ██║ ╚██████╔╝ ╚██████╗ ██║  ██╗
╚═╝  ╚═╝  ╚═════╝   ╚═════╝ ╚═╝  ╚═╝
        R O C K

██████╗   █████╗  ███████╗ ███████╗ ██████╗ 
██╔══██╗ ██╔══██╗ ██╔════╝ ██╔════╝ ██╔══██╗
██████╔╝ ███████║ █████╗   █████╗   ██████╔╝
██╔═══╝  ██╔══██║ ██╔══╝   ██╔══╝   ██╔══██╗
██║      ██║  ██║ ███████╗ ███████╗ ██║  ██║
╚═╝      ╚═╝  ╚═╝ ╚══════╝ ╚══════╝ ╚═╝  ╚═╝
        P A P E R

███████╗ ██╗ ███████╗ ███████╗  ██████╗  ██████╗ 
██╔════╝ ██║ ██╔════╝ ██╔════╝ ██╔═══██╗ ██╔══██╗
███████╗ ██║ ███████╗ ███████╗ ██║   ██║ ██████╔╝
╚════██║ ██║ ╚════██║ ╚════██║ ██║   ██║ ██╔══██╗
███████║ ██║ ███████║ ███████║ ╚██████╔╝ ██║  ██║
╚══════╝ ╚═╝ ╚══════╝ ╚══════╝  ╚═════╝  ╚═╝  ╚═╝
        S I S S O R
""")

    human = input("Enter: ").strip() .title()
    
    if human == "Rock":
        print("""
    Human
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif human == "Paper":
        print("""
    Human
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif human == "Sissor":
        print("""
    Human
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    else:
        print("Invalid Input")
        return

    computer = random.choice(["Rock", "Paper", "Sissor"])

    if computer == "Rock":
        print("""
    Computer
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif computer == "Paper":
        print("""
    Computer
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif computer == "Sissor":
        print("""
    Computer
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

    # Determine winner
    if human == "Rock" and computer == "Rock":
        print("Tie")
        Menu()
    elif human == "Rock" and computer == "Paper":
        print("Human Lose/Computer Win")
        Menu()
    elif human == "Rock" and computer == "Sissor":
        print("Human Win/Computer Lose")
        Menu()
    elif human == "Paper" and computer == "Rock":
        print("Human Win/Computer Lose")
        Menu()
    elif human == "Paper" and computer == "Paper":
        print("Tie")
        Menu()
    elif human == "Paper" and computer == "Sissor":
        print("Human Lose/Computer Win")
        Menu()
    elif human == "Sissor" and computer == "Rock":
        print("Human Lose/Computer Win")
        Menu()
    elif human == "Sissor" and computer == "Paper":
        print("Human Win/Computer Lose")
        Menu()
    elif human == "Sissor" and computer == "Sissor":
        print("Tie")
        Menu()

def Menu():
    select = input("\nTry Again?\nYes or No\nEnter:").strip() .title()
    
    if select == "Yes":
        rps()
    elif select == "No":
        print("Thank you for playing have a great day!")

rps()