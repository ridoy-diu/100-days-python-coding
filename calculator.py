def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculation = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

# print(calc_dictionary["*"](4,5))

def calculator():

    should_continue = True
    first_num = float(input("Type the first number: "))

    while should_continue:

        for key in calculation:
            print(key)
        operator = input("Choose an operator: ")
        second_num = float(input("Type the next number: "))

        result = calculation[operator](first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {result}")

        continue_calc = input(f"Do you want to continue with the previous result {result}? Type 'y' for YES or 'n' for NO.\n").lower()

        if continue_calc == "y":
            first_num = result
        else:
            should_continue = False
            print("\n" * 50)
            calculator()

calculator()