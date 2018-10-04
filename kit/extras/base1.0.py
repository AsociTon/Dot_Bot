import databases
from databases import dbase
import re
import random


from phrase import welcome_phrases
dbase.create_table()


print("Hi, sir")
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
                abs=1
                tiger = welcome_phrases.lib_name.index(p)
                break

#Process_choices Names
#Process choices fo
#Process choices fr
#process choices reg

while abs==1 :
    abs=2
    for p in welcome_phrases.lib_name:
        for q in p:
            for r in wordList :
                if r.lower == q:
                    tiger = welcome_phrases.lib_name.index(p)
                    break
    print(random.choice(welcome_phrases.process_choices_name[tiger]))
    intro_in=input("")
    wordList = re.sub("[^\w]", " ", intro_in).split()
    for p in welcome_phrases.lib_name:
        for q in p:
            for r in wordList:
                if r.lower()==q :
                    abs=1
                    break

for i in welcome_phrases.lib_intro:
    for j in i:
        for k in wordList:
            if k.lower() == j:
                trigger = welcome_phrases.lib_intro.index(i)
                break

print(random.choice(welcome_phrases.process_choices_fo[trigger]))
sad = ["Enter your name", "Enter your city ", "Enter your state", "Enter pincode of your area", "Enter your locality", "Enter your mobile number","Enter your aadhaar number"]
ans = []
if trigger == 0:
    intro_in = input("Which form do you want\n")
    for k in welcome_phrases.lib_form:
        for l in k:
            if intro_in.lower() == l:
                lion = welcome_phrases.lib_form.index(k)
                break
    print(random.choice(welcome_phrases.process_choices_fr[lion]))
    for sd in sad:
        ans.append(input(sd))
    for x in range(7):
        print("You have applied for " + intro_in + "\n" + sad[x] + " -> " + ans[x])
    check = input("Do you want to continue?[yes/no]")
    if check == "yes":
        print("Thankyou for using our service!")
        dbase.insert_value(ans[0], ans[1], ans[2], ans[3], ans[4], ans[5], ans[6], generate_ucode())
    elif check == "no":
        print("We cancelled your request")
    else:
        print("Please specify clearly")


elif trigger == 1:
    intro_in = input("Which registration do you want\n")
    for k in welcome_phrases.lib_reg:
        for l in k:
            if intro_in.lower() == l:
                lion = welcome_phrases.lib_reg.index(k)
                break
    print(random.choice(welcome_phrases.process_choices_reg[lion]))
    for sd in sad:
        ans.append(input(sd))
    for x in range(6):
        print("You have applied for " + intro_in + "\n" + sad[x] + " -> " + ans[x])
    check = input("Do you want to continue?[yes/no]")
    if check == "yes":
        print("Thankyou for using our service!")
        dbase.insert_value(ans[0], ans[1], ans[2], ans[3], ans[4], ans[5], ans[6], generate_ucode())
    elif check == "no":
        print("We can cancelled your request")
    else:
        print("please enter right choice")
elif trigger == 2 :
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
else:
    print("Wrong choice")
print("Here is your token number\n")
print("Date Time")
print("\ntake it to the nearest government office and enjoy!\n")
print("Thank you, for using our services!")

