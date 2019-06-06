def get_float(text):
    while True:
        v = input(text)
        try:
            v = float(v)
            return v
        except ValueError:
            print('That value in invalid!')


while True:
    user_operator = input("What is the operation you'd like to perform?\n")
    if user_operator.upper() == 'DONE':
        break

    user_input1 = get_float("What is the first number?\n")
    user_input2 = get_float("What is the second number?\n")


    if user_operator in '+-*/':
        if user_operator == '+':
            print("The result is: " +str(user_input1 + user_input2))
        elif user_operator == '-':
            print("The result is: " +str(user_input1 - user_input2))

        elif user_operator == '*':
            print("The result is: " +str(user_input1 * user_input2))
        elif user_operator == '/':
            print("The result is: " +str(user_input1 / user_input2))
    else:
        print('That is not a valid operator')
