#!/bin/python3
# argv - it is argument in python
import sys # system library
from datetime import datetime as dt # import with alias
print (dt.now())

my_name = "Vadym"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence"
print(sentence[:4])

print(sentence.split()) # delimeter space by default

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, \"give me all your money\"" # slash make character to ignore them
print(quote)

too_much_space = "                      Hello"
print(too_much_space.strip())

print("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

movie = "The Hangover"
print("My favorite movie is {}".format(movie))

#Dictionaries - key/value pairs {}
drinks = {"White Russian" : 7, "Old Fashion" : 10, "Lemon Drop" : "8"} #drink is key, price is value
print(drinks)

employees = {"Finance" : ["Bob", "Linda", "Tina"], "IT" : ["Gene","Louise","Teedy"], "HR" : ["Jimmy Jr.","Mort"]}
print(employees)

employees['Legal'] = ['Mr.Frond'] #add a new key/value pair
print(employees)

employees.update({"Sales" : ["Andie", "Olie"]}) #add a new key/value pair
print(employees)

drinks["White Russian"] = 8 #update value
print(drinks)
print(drinks.get("White Russian"))#print choosen value
