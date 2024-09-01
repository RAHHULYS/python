import art
def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2


operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(art.calculator_logo)
    n1 = int(input("Enter the first number:"))
    should_accumulate = True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick an operation: ")
        n2 = int(input("Enter the second number: "))
        answer = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        choice = input(f"Type 'Y' to continue calculating with {answer} or type 'n' to start new calculation:").lower()
        if choice == "y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n" *20)
            calculator()
calculator()
