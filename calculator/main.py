from art import logo

print(logo)

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2


operator = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

for oper in operator:
    print(oper)
operation_symbol = input("Pick an operation from the line above: ")

calculate = operator[operation_symbol] # operator[operation_symbol] accesses add.
# then () added to it with 2 arguments will call the function and calculate the result/return it
answer = calculate(n1, n2)

print(f"{n1} {operation_symbol} {n2} = {answer}")

