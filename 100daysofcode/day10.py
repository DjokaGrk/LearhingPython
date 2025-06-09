# def format_name(f_name, l_name):
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f"{f_name} {l_name}"
#
# first = input("Enter your first name: ")
# last = input("Enter your last name: ")
# # primer 1
# formatted_name = format_name(first, last)
# print(formatted_name)
# # primer 2
# print(format_name(first, last))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)