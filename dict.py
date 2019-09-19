import json
import difflib
from difflib import get_close_matches
data = json.load(open('data.json'))
def lookup():
    a = input("Please enter a word: ").lower()
    if a in data:
        return data[a]
    elif len(get_close_matches(a, data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(a, data.keys())[0]).lower()
        if yn == "Y".lower():
            return data[get_close_matches(a,data.keys())[0]]
        elif yn == "N".lower():
            return "This word does not exist"
        else:
            return "We didn't understand your quary"
    else:
        return "Word does not exist in this dictionary"



test = lookup()
num = 1
if type(test) == list:
    for i in test:
        print(str(num)+ " " +i)
        num+=1
else:
    print(test)
