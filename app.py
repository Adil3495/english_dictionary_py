import json
from difflib import get_close_matches


data = json.load(open("Data/data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:  # title like "delhi" to "Delhi"
        return data[w.title()]
    elif w.upper() in data:  # in case user enter USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        yn = input(
            f"Did you mean {get_close_matches(w, data.keys(), cutoff=0.8)[0]} instead ? Enter Y if yes, or N if no : ")
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")

output = translate(word)

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)
