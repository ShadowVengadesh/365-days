import json
from difflib import get_close_matches
myfile=json.load(open("data.json"))

def check(d):
    d=d.lower()
    if d in myfile:

        return myfile[d]
    elif len(get_close_matches(d,myfile.keys()))>0:
        return "did you mean %s" %get_close_matches(d,myfile.keys())[0]
    else:
        print("please enter the correct value")
        return ""
word=input("enter the word:")
print(check(word))