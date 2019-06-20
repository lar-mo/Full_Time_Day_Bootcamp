# filename: lab15_functions.py
'''
This file contains two functions: get_integer() and run_tests().
    • get_integer() is for getting and validating the user input (integer).
    • run_tests() is for the units tests embedded in the bottom of the lab 15 solutions.
'''

'''
### GET INTEGER ###
This function takes two parameters: user input prompt text (string) and upper_range_limit (integer)
e.g.
"Enter a number between 0 - 99 to convert: "
'''

def get_integer(prompt_text, upper_range_limit):
    error_msg = f"That's not a number between 0 - {upper_range_limit}. Try again."
    while True:
        try:
            num = int(input(prompt_text))
            if num < 0 or num > upper_range_limit:
                print(error_msg)
            else:
                return num
        except ValueError:
            print(error_msg)

'''
### RUN TESTS ###
This function takes two parameters: user input (integer) and expected output
from a list of tuples.
e.g.
[(7, "seven"), (17, "seventeen"), (77, "seventy seven")]            # lab 15, v1
((107, "one hundred seven"), (777, "seven hundred seventy seven")]  # lab 15, v2
[(7, "VII"), (17, "XVII"), (77, "LXXVII"), (777, "DCCLXXVII")]      # lab 15, v3

If any tests fail, a descriptive message is returned and printed.
Otherwise, "All tests passed." is returned and printed.
'''

def run_tests(input_output, lab_name):
    failed_test_count = 0
    for i in range(len(input_output)):
        input = lab_name(input_output[i][0])
        expected_output = input_output[i][1]
        if input != expected_output:
            return f"{input}: Fail. Expected Result: {expected_output} ==> Actual result: {input}"
            failed_test_count += 1
    if failed_test_count == 0:
            return "All tests passed."
