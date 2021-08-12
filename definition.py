'''
This is a program that gives multiple definitions of some word.
'''

import json
from difflib import get_close_matches


def translate(word):
    if word in dictionary:
        return dictionary[word]
    elif word.capitalize() in dictionary:
        return dictionary[word.capitalize()]
    elif word.upper() in dictionary:
        return  dictionary[word.upper()]
    elif len(get_close_matches(word, dictionary.keys())) > 0:
        match = get_close_matches(word, dictionary.keys())[0]
        answer = input(f"Did you mean: {match}? Yes or No? ").lower()
        if answer == "yes":
            return dictionary[match]
        elif answer == "no":
            return "This word doesn't exist. Please double check it."
        else:
            return "We don't understand your entry."
    else:
        return "This word doesn't exist. Please double check it."


dictionary = json.load(open("data.json"))

word = input("Give me a word to get a definition of: ").lower()
output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
