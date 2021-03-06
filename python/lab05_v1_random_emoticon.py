# filename: lab05_v1_random_emoticon.py
'''
Lab 5: Random Emoticon Generator

Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
'''

import random

# Define a list of eyes
eyes = [':', ';', '=']
# Define a list of noses
noses = ['-', '^', 'o']
# Define a list of mouths
mouths = ['(', ')', '/']
# Randomly pick a set of eyes
eye = random.choice(eyes)
# Randomly pick a nose
nose = random.choice(noses)
# Randomly pick a mouth
mouth = random.choice(mouths)

# Assemble and display the emoticon
print(eye + nose + mouth)
