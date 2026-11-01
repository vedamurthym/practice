a=input("enter your email:")
def email(a):
    if a == "vedamurthy1123@gmail.com"==a:
        print("valid email")
    else:
        print("invalid email")
email(a)


s=input("enter your name:")
c=0

def capital(s):
    for ch in s:
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            c+=1
        print("number of capital letters:",c)
capital(s)


p=str(input("enter your password:"))
def password(p):
    if len(p) >= 8:
        print("valid password")
    else:
        print("invalid password")   
password(p)
