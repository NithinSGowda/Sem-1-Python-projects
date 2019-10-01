#Password Checker and Generator
def checker():
    def check_upper (in_str):
        Upper_Case = set ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")    
        return in_str & Upper_Case

    def check_lower (in_str):
        Lower_Case = set ("abcdefghijklmnopqrstuvwxyz")    
        return in_str & Lower_Case

    def check_numerals (in_str):
        Numerals = set ("0123456789")    
        return in_str & Numerals

    def check_special (in_str):
        Special_Case = set ("$#@!%^&*")    
        return in_str & Special_Case
    
    pwd = input ("Enter Your password : ")
    pwds = set (pwd)
    res=[]
    if check_upper (pwds):
        res.append(1)
    else:
        print("You could have included a Uppercase character")
    if check_lower (pwds):
        res.append(1)
    else:
        print("You could have included a Lowercase character")
    if check_numerals (pwds):
        res.append(1)
    else:
        print("You could have included a Number")
    if check_special (pwds):
        res.append(1)
    else:
        print("You could have included a Special character")
    if len(pwd)>8:
        res.append(1)
    else:
        print("Your password should have been more than 8 characters ")
    print()
    print("The strenght of your present password ",pwd," is ",sum(res)*20,"%")
    
def generator():
    import random
    pwd=""
    for i in range(0,2):
        pwd = pwd + chr(random.randint(65,90))
        pwd = pwd + chr(random.randint(97,122))
        pwd = pwd + chr(random.randint(48,57))
        pwd = pwd + chr(sum(random.sample([33,64,35,36,37,38],1)))
    print(pwd," is your new password")
print("Welcome to password generator and checker software")
print("Click 0 to check the strenght of your password ")
print("Click 1 to generate a new password ")
aa=int(input())
if aa==0:
    checker()
elif aa==1:
    generator()
else :
    print("Enter valid choice and retry")
         



