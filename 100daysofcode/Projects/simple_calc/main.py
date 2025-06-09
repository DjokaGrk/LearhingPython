from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2
calc_dic = {
'+' : add,
'-' : subtract,
'*' : multiply,
'/' : divide,
}
print(calc_dic['+'](4, 8))