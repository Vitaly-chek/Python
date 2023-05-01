import sys
# compare = 3 == 4
# print(compare)
#
#
# x = 5
# print(f"Result_1 = {x > 3 and x > 8}")
# print(f"Result_2 = {x > 3 and not x > 8}")
# print(f"Result_3 = {x > 3 or x > 8}")

# c = int(input("Enter the number: "))
# if c == 5:
#     print("Yes, c = 5")
# else:
#     print("No, c != 5")

# Homework, program calculation
try:
    num_1 = float(input("Enter the number_1: "))
    num_2 = float(input("Enter the number_2: "))
except ValueError:
    print("---------------------- \n|Введіть чилсо!!!!!!!|\n---------------------- \n")
    sys.exit()

operator = input(f"You can type operator: \n '/' - Delenie \n '*' - Umnojenie \n '+' - Plus \n '-' - Minus \n Enter the operator: ")

if operator == '/':
    try:
        result = num_1 / num_2
        print(f"Result '/' = {result}")
    except ZeroDivisionError:
        print("------------------------ \n|На нуль ділити неможна| \n------------------------")
elif operator == '*':
    result = num_1 * num_2
    print(f"Result '*' = {result}")
elif operator == '+':
    result = num_1 + num_2
    print(f"Result '+' = {result}")
elif operator == '-':
    result = num_1 - num_2
    print(f"Result '-' = {result}")
else: print("Введено невірний оператор. Оберіть оператор зі списку!!")
