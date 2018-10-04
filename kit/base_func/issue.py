from phrase import welcome_phrases
import random
from . import ucode
from databases import dbase
from phrase import issue_data
import re
from databases import issue_base

done = int()

def default_issue(issue, aadhnum, dotkey):
    print(".bot >> your issue is:\n"+issue)
    print(".bot >> please categorise it")
    it = input(".bot >> issue type:")
    sit = input(".bot >> issue sub type:")
    issue_base.insert_value(it, sit, issue, aadhnum, dotkey)
    print(".bot >> your issue has been registered under category "+it+" \nsubcategory"+sit)





def checkissue(issue,aadhnum,dotkey):
    trigger = int()
    foundat = int()
    wordList = re.sub("[^\w]", " ", issue).split()
    for i in issue_data.issue_type:
        for j in wordList:
            if i == j:
                trigger = 0
                foundat = i
            else:
                trigger = 1
    if foundat == 1:
        for i in issue_data.issue_0:
            for j in wordList:
                i == j

    if trigger == 0:
        print(".bot >> your issue has been registered under")
        print(issue_data.issue_type(trigger) +" categorised under " + issue_data.issue_electric_type(trigger))
        x = input(".bot >> was I able to round it up?")
        if x == "yes":
            print(".bot >> Happy to help you")
            issue_base.insert_value(issue_data.issue_type(trigger), issue_data.issue_electric_type(trigger), issue, aadhnum, dotkey)
            done = 1
    else:
            print(".bot >> Maybe you can specify it clearly than us")
            default_issue(issue, aadhnum, dotkey)




def fileissue(choice):
    if choice==1:
        while True:
            dotkey = input(".bot >> enter Your Dotkey : ")
            adm = input(".bot >> enter your aadhaar number : ")
            val = dbase.validate(dotkey)
            print(val)
            if val(0) == adm:
                # print("your records are:")
                # todo print record via view
                ans = input(".bot >> state your issue freely : ")
                checkissue(ans, adm, dotkey)
                done = 1
                break
            else:
                print(".bot >> we checked our databases, either the dotkey or the aadhaar number is incorrect!")
                print(".bot >> respecify the data ")
                continue
    else:
        dotkey = ucode.generate_ucode()
        while True:
            aadhaarnumber = input(".bot >> enter your aadhaar number:")

            if not aadhaarnumber.isnumeric():
                print(".bot >> an aadhaar number has numeric characters only")
                continue

            if not len(aadhaarnumber) == 12:
                print(".bot >> invalid aadhaar number , please make sure your aadhaar number is of 12 digits")
                continue
            else:
                break
        print(".bot >> your dotkey for this query is \n"+dotkey)
        print(".bot >> keep your dotkey safely for further queries to this issue")
        ans = input(".bot >> state your issue freely : ")
        checkissue(ans, aadhaarnumber, dotkey)


#main function to be called
def issuein():
    print(".bot >> Before registering your issue ,"
          "\nkindly tell us have you got the dot key of an exsisiting SAPF?"
          "it will ease the process for both of us")
    check = input("yes/no")
    if check.lower() == "yes":
        fileissue(1)
        
    elif check.lower() == "no":
        fileissue(0)
    else:
        print(".bot >> please specify clearly your reply was no or yes..\n")



if done == 1:
    print(".bot >> Sorry for the problem you suffered we will be working on sorting it soon")

