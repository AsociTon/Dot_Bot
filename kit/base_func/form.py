from . import ucode
from databases import dbase

def formin(lion=0):
    print(".bot >> This is the SAPF section,\n"
          "     please enter your details carefully")
    sapfcode = []


    from form_layout import formin
    ans = formin.formstruct

    check = input(".bot >> Do you want to continue?[yes/no]")
    if check == "yes":
        print("Thankyou for using our service!")
        sapfcode = ucode.generate_ucode()
        dbase.insert_value(ans.name, ans.city, ans.state, ans.pincode, ans.pincode, ans.mobilenumber, ans.aadhaarnumber, sapfcode)
        print(".bot >> Here is your unique dot key\n")
        print(sapfcode)
        print("\n       take it to the nearest government office and you can retrieve all your data!\n")
        print("       Thank you, for using our services!")
    elif check == "no":
        print(".bot >> We cancelled your request\n")
    else:
        print(".bot >> Please specify clearly\n")


