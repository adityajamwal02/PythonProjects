#!/usr/bin/env python
# coding: utf-8

# # QUIZ GAME

# In[ ]:


print("Welcome All")
playing = input("Do you want to start the game? ")
if playing.lower() != "yes":
    quit()

print('Lets Begin')

count=0;

answer=input("What does CPU stand for ")
if answer.lower() == "central processing unit":
    print("Correct")
    count+=1;
else:
    print("Incorrect")

answer=input("What is capital of Netherlands ")
if answer.lower() == "amsterdam":
    print("Correct")
    count+=1;
else:
    print("Incorrect")
    
answer=input("Who is referred as 'The Flying Sikh' ")
if answer.lower() == "milka singh":
    print("Correct")
    count+=1;
else:
    print("Incorrect")
    
answer=input("What is capital of Jamaica ")
if answer.lower() == "kingston":
    print("Correct")
    count+=1;
else:
    print("Incorrect")

answer=input("What does SMS stand for ")
if answer.lower() == "short message service":
    print("Correct")
    count+=1;
else:
    print("Incorrect")
    
print(" Your Score : " + str(count) + "!")
print(" Your Percent: " + str((count/5)*100) + "%")

