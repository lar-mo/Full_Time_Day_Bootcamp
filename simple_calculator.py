while True:
    user_operator = input("What is the operation you'd like to perform?\n")
    if user_operator.upper() == 'DONE':
        break
        
    user_input1 = float(input("What is the first number?\n"))
    user_input2 = float(input("What is the second number?\n"))


    if user_operator in '+-*/':
        if user_operator == '+':
            print("The result is: " +str(user_input1 + user_input2))
        elif user_operator == '-':
            print("The result is: " +str(user_input1 - user_input2))

        elif user_operator == '*':
            print("The result is: " +str(user_input1 * user_input2))
        elif user_operator == '/':
            print("The result is: " +str(user_input1 / user_input2))
