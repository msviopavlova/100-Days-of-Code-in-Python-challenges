def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1-num2


def multiply(num1, num2):
    return num1*num2


def divide(num1, num2):
    return num1/num2


operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate():
    from art import logo
    print(logo)

    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    for oper in operator:
        print(oper)

    operation_symbol = input("Pick an operation from the line above: ")
    calculator = operator[operation_symbol]   # operator[operation_symbol] accesses add.

    # then () added to it with 2 arguments will call the function and calculate the result/return it
    answer = calculator(n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")

    keep_counting = True
    while keep_counting:
        new_operator_or_stop = input("Enter next operator or type 'new' to start again ")

        if new_operator_or_stop == "new":
            keep_counting = False
            calculate()
        else:
            n3 = float(input("Enter another number: "))
            new_answer = operator[new_operator_or_stop](answer, n3)
            print(new_answer)

calculate()