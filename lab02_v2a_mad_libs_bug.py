# Lab02: version 2
# ask the user for 3 adjectives, separated by commas, then use the .split() function

# Ask the user for 3 adjectives, separated by commas
three_adj = '' # base case
for num in range(0,3):
    user_adj = input("Enter an adjective: ")
    # create a list of adjectives (string)
    three_adj += user_adj
    if num < 2:
        three_adj += ','

print(f"before split: three_adj={three_adj}") #debug print statement

# VERSION 1: Use the .split() function to store each adjective
list_adj = three_adj.split(",") # issue 1: without pop(), there is a fourth item ",".

print(f"Version 1: after split: list_adj={list_adj} - an empty list item due to trailing comma in three_adj string.") #debug print

# VERSION 2: Use the .split() function to store each adjective
list_adj = three_adj.split(",",2) # issue 2: with .split(",",2)

print(f"Version 2: after split: list_adj={list_adj} - the trailing comma is part of list_adj[2]") #debug print

'''
OUTPUT:
MacBook-Air-2:Day-Time_Full_Bootcamp larrymoiola$ py lab02_v2a_mad_libs_bug.py
Enter an adjective: a
Enter an adjective: b
Enter an adjective: c
before split: three_adj=a,b,c,
Version 1: after split: list_adj=['a', 'b', 'c', ''] - an empty list item due to trailing comma in three_adj string.
Version 2: after split: list_adj=['a', 'b', 'c,'] - the trailing comma is part of list_adj[2]
'''
