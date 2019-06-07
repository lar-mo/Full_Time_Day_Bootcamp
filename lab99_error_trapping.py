my_dict = {'key': 'value'}
while True:
    user_input = input ("Type 'key': ")
    try:
        print(my_dict[user_input])
        break
    except KeyError:
        print('wrong')

while True:
    user_num = input('Type a number: ')
    if user_num.isdigit():
        print(int(user_num) + 1)
        break
