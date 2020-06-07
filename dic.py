import json
import difflib
from difflib import get_close_matches 


data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]    
             
    elif len(get_close_matches(word,data.keys())) > 0 :
        answer=input("did you mean %s?(yes/no): " %get_close_matches(word,data.keys())[0])
        if(answer == "yes"):
              return data[get_close_matches(word,data.keys())[0]]
        elif(answer == "no"):
             return "no such word exists"
        else:
             return "we did not understand your query"           
    else:
        return "this word doesnt exist"


word=input("enter the word: ")
output=translate(word)
if type(output)==list:
   for i in output:
      print(i)
else:
   print(output)   
