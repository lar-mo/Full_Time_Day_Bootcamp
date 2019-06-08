numbers_dict = {} # set base case (dictionary)
# While loop: populate the new dictionary from user input
while True:
    userinput_num = input("Enter a number, or 'done': ")
    if userinput_num == "done":
        break
    if userinput_num in numbers_dict:
        # if the user enters a number that already exists, increment the count by 1
        numbers_dict[userinput_num] += 1
    else:
        # if the user enters a number that does not yet exist, set count = 1
        numbers_dict[userinput_num] = 1

# *** NEEDS MORE CLARIFICATION ***
counts = list(numbers_dict.items()) # .items() returns a list of tuples
counts.sort(key=lambda tup: tup[1], reverse=True) # sort largest to smallest, based on count
# print(numbers_dict)
# print(counts)

highest_count = 0 # set base case (integer)
highest_num = '' # set base case (string)
for num in numbers_dict:
    if numbers_dict[num] > highest_count:
        highest_count = numbers_dict[num]
        highest_num = num

print("\n")
print("OUTPUT")
print(f"For Loop (list): Your preferred the number is {highest_num}.")
print(f"Tuple: Your preferred the number is {counts[0][0]}.")
print("\n")