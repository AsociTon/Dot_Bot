from phrase import welcome_phrases
import random
import re
from databases import dbase
from . import ucode


def registerin():
    intro_in = input("Whats your issue\n")
    while abs == 1:
        abs = 2
        for p in welcome_phrases.lib_issue:
            for q in p:
                for r in wordList:
                    if r.lower == q:
                        tiger = welcome_phrases.lib_name.index(p)
                        break
        print(random.choice(welcome_phrases.process_choices_issue[tiger]))
        intro_in = input("")
        wordList = re.sub("[^\w]", " ", intro_in).split()
        for p in welcome_phrases.lib_name:
            for q in p:
                for r in wordList:
                    if r.lower() == q:
                        abs = 1
                        break
    print("Is this your issue?->\n")
    print(intro_in)
    check = input("Do you want to continue?[yes/no]")
    if check == "yes":
        print("Thank you, for using our service!")
    elif check == "no":
        print("We can cancelled your request")
    else:
        print("please enter right choice")