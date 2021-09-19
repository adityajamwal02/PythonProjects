'''
The Following Program relates a given string to leet language. (leetspeak). 
Author: ADITYA JAMWAL
'''
# Importing Module
import random

# Function
def converttoleet(msg):
    message=""
    charMapping = { 'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'], 'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'], 'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'], 'v': ['\\/']}
    for i in msg:
        if(i in charMapping.keys() and random.random()<=0.7):
            change=charMapping.get(i," ")
            message+=random.choice(change)
        else:
            message+=i
    return message


stringIn=input("Type Your Message: ").lower()
stringOut=converttoleet(stringIn)
print("\n Normal Message: {} \n LeetCode: {}".format(stringIn,stringOut))