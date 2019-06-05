my_dict = {'key': 'value'}
while True:
    user_input = input ('Type key: ')
    try:
        print(my_dict[user_input])
        break
    except KeyError:
        print('wrong')
