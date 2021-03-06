# filename: lab10_v2_average_numbers.py
'''
Lab 10: Average Numbers

Version 2
Ask the user to enter the numbers one at a time, putting them into a list.
If the user enters 'done', then calculate and display the average.
The following code demonstrates how to add an element to the end of a list.

nums = []
nums.append(5)
print(nums)
Below is an example input/output:

> enter a number, or 'done': 5
> enter a number, or 'done': 3
> enter a number, or 'done': 4
> enter a number, or 'done': done
average: 4
'''

# Ask the user to enter the numbers one at a time, putting them into a list.
# If the user enters 'done', then calculate and display the average.

nums = []
while True:
    userinput_num = input("Enter a number, or 'done': ")
    if userinput_num == "done":
        if len(userinput_num) > 0:
            break
    else:
        nums.append(int(userinput_num))

# iterate through the list
# Keep a 'running sum'
num = 0
for i in range(len(nums)):
    num += nums[i]

# Divide that sum by the number of elements in that list
my_average = num / len(nums)
print(f"Average: {my_average}")
