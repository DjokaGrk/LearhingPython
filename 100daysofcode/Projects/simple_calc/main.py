from art import logo
print(logo)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

calc_dic = {
'+' : add,
'-' : subtract,
'*' : multiply,
'/' : divide,
}
def get_input(prompt):
    value = input(prompt)
    if value.lower() == 'close':
        print("Calculator closed.")
        exit()
    return value

def calc ():
    n1 = float(get_input("Enter the first number (or type 'close' to exit): "))
    operator = get_input('Enter operator "+", "-", "*", or "/" (or type "close" to exit): ')
    n2 = float(get_input("Enter the second number (or type 'close' to exit): "))

    while operator not in calc_dic:
        print("invalid operator")
        operator = input('pls enter valid operator choice is: "+", "-", "*" or "/") ')
    result = calc_dic[operator](n1, n2)
    print(f"{n1} {operator} {n2} = {result}")
    while True:
        next_calc = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or any other key to exit: ").lower()
        if next_calc == 'y':
            operator = input('pls enter next operator choice is: "+", "-", "*" or "/" or type "close" to exit): ')
            while operator not in calc_dic:
                operator = input('pls enter next operator choice is: "+", "-", "*" or "/" or type "close" to exit): ')
            nxt_number = float(input("Enter the next number: "))
            result_before = result
            result = calc_dic[operator](result, nxt_number)
            print(f"{result_before} {operator} {nxt_number} = {result}")

        elif next_calc == 'n':
            calc()  # recursive restart
            break
        else:
            break

calc()