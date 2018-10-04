
'''  intro_in = input("Which form do you want\n")
    for k in welcome_phrases.lib_form:
        for l in k:
            if intro_in.lower() == l:
                lion = welcome_phrases.lib_form.index(k)
                break
    print(random.choice(welcome_phrases.process_choices_fr[lion]))
for sd in welcome_phrases.sad:
ans.append(input(sd))
   '''

issue
sapfcode = []
    intro_in = input("Which registration do you want\n")
    for k in welcome_phrases.lib_reg:
        for l in k:
            if intro_in.lower() == l:
                lion = welcome_phrases.lib_reg.index(k)
                break
    print(random.choice(welcome_phrases.process_choices_reg[lion]))
    for sd in welcome_phrases.sad:
        ans.append(input(sd))
    for x in range(6):
        print("You have applied for " + intro_in + "\n" + welcome_phrases.sad[x] + " -> " + ans[x])
    check = input("Do you want to continue?[yes/no]")
    if check == "yes":
        print("Thankyou for using our service!")
        sapfcode = ucode.generate_ucode()
        dbase.insert_value(ans[0], ans[1], ans[2], ans[3], ans[4], ans[5], ans[6], sapfcode)
        print("Here is your token number\n")
        print(sapfcode)
        print("\ntake it to the nearest government office and enjoy!\n")
        print("Thank you, for using our services!")
    elif check == "no":
        print("We can cancelled your request")
    else:
        print("please enter right choice")
