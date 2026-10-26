import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if word  in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn= input(f"Did you mean: '{get_close_matches(w, data.keys())[0]}'. Enter Y for Yes and N for No : ")
        if yn=="Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn=="N":
            return "Word not found."
        else:
            return "Did not understand."
    else:
        return "Word not found!"

while True:
    word = input("Enter Word: ")
    output = translate(word)
    for item in output:
        print(item)