import databases
from databases import dbase
from base_func import form
from base_func import issue
from base_func import register
import datetime
import re
import random


from phrase import welcome_phrases


dbase.create_table()

intro_in = str()
# FOR TAKING TASk
while(intro_in!="break") :
    def space():
        for i in range(0, 5):
            print(" ")


    print(".bot >> Hi, sir")
    print("I am Dot_Bot \n"
          "I can assist you with filling SINGLE ALL PURPOSE FORM (SAPF), registering with queries related to electricity and Driving License")
    print("Select 1)Forms\n2)Register\n3)Issues")
    intro_in = input("What can i do!\n")
    wordList = re.sub("[^\w]", " ", intro_in).split()
    trigger = int(0)
    lion = int(0)
    tiger = int(0)
    abs = int(0)
    for i in welcome_phrases.lib_intro:
        for j in i:
            for k in wordList:
                if k.lower() == j:
                    break
            trigger += 1
    for p in welcome_phrases.lib_name:
        for q in p:
            for r in wordList:
                if r.lower() == q:
                    abs = 1
                    tiger = welcome_phrases.lib_name.index(p)
                    break

    # Process_choices Names
    # Process choices fo
    # Process choices fr
    # process choices reg

    while abs == 1:
        abs = 2
        for p in welcome_phrases.lib_name:
            for q in p:
                for r in wordList:
                    if r.lower == q:
                        tiger = welcome_phrases.lib_name.index(p)
                        break
        print(random.choice(welcome_phrases.process_choices_name[tiger]))
        intro_in = input("")
        wordList = re.sub("[^\w]", " ", intro_in).split()
        for p in welcome_phrases.lib_name:
            for q in p:
                for r in wordList:
                    if r.lower() == q:
                        abs = 1
                        break

    for i in welcome_phrases.lib_intro:
        for j in i:
            for k in wordList:
                if k.lower() == j:
                    trigger = welcome_phrases.lib_intro.index(i)
                    break

    print(random.choice(welcome_phrases.process_choices_fo[trigger]))

    ans = []
    if trigger == 0:
        form.formin()

    elif trigger == 1:
        issue.issuein()

    elif trigger == 2:
        issue.issuein()

    else:
        print("Wrong choice")
    intro_in = input("Do you want anything else?\nIf you want to exit just type 'break'")
print("Thankyou for using our services")


