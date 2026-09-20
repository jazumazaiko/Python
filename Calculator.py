print(r"""
  ____      _            _       _
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |__| (_| | | (__| |_| | | (_| | || (_) | |
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
 """)
print("""
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")

def calculate(operator):
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    if operator == 1:
        result = num1 + num2
        print(f"Result:{result}")
        calculator()
    elif operator == 2:
        result = num1 * num2
        print(f"Result:{result}")
        calculator()
    elif operator == 3:
        result = num1 / num2
        print(f"Result:{result}")
        calculator
    elif operator == 4:
        result = num1 - num2
        print(f"Result:{result}")
        calculator
    else:
        print("Invalid input please try again")
        calculator()
        
def calculator():
    operator = int(input("Type the number of the operator:\n1. Addition\n2. Multiplicarion\n3. Division\n4. Subtraction\nEnter:"))
    calculate(operator)
    
calculator()