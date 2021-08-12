'''
This is a program that gives multiple definitions of some word.
'''

import json

def translate(word):
    if word in dictionary:
        return dictionary[word]
    else:
        return "Wrong input."


dictionary = json.load(open("data.json"))

word = input("Give me a word to get a definition of: ").lower()
output = translate(word)

if type(output) == list:
    definition_number = 1
    for i in output:
        print("Definition" + str(definition_number) + ": " + i)
        definition_number += 1
else:
    print(output)