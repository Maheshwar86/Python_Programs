import re


def Email_Slicer():
    email = input("Please Enter A Your Email Or Gmail : ")
    pat = "@"
    res = re.search(pat,email)
    if res != None:
        print(f"User Name Is : {email[:email.index("@")]} ")
        print(f"Domain Is : {email[email.index("@")+1:]}")
    else:
        print("Invalid Email Address ! ")
        Email_Slicer()
Email_Slicer()