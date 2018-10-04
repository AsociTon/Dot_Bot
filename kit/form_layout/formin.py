class formstruct():
    name = str()
    while True:
     name = input("\n.bot >> enter your first name:")

     if not name.isalpha():
         print(".bot >> your first name must have alphabets only!")
         continue
     else:
         name = name.upper()
         break

    city = str()
    while True:
        city = input("\n.bot >> enter your city:")

        if not city.isalpha():
            print(".bot >> a city name can have alphabets only!")
            continue
        else:
            city = city.upper()
            break

    state = str()
    while True:
        state = input(".bot >> which sate do your reside in?")

        if not state.isalpha():
            print(".bot >> a state name can have alphabets only!")
            continue
        else:
            state = state.upper()
            break

    pincode = str()
    while True:
        pincode = input(".bot >> pincode of your area?")

        if not pincode.isnumeric():
            print(".bot >> a pincode has numeric characters only")
            continue

        if not len(pincode)==6:
            print(".bot >> invalid pincode , please make sure your pincode is of 6 digits")
            continue
        else:
            break

    mobilenumber = str()
    while True:
        mobilenumber = input(".bot >> provide us the mobile number we can contact you with?")

        if not mobilenumber.isnumeric():
            print(".bot >> a mobile number has numeric characters only")
            continue

        if not len(mobilenumber) == 10:
            print(".bot >> invalid mobile number , please make sure your mobile number is of 10 digits")
            continue
        else:
            break
    aadhaarnumber = str()
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





    def __init__(self,val):
        print("In Class Method")
        self.val = val
        print("The Value is: ", val)




