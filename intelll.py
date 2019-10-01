import random
print()
print()
print("Welcome to real Intelligience software devloped by Nithin.S")
print()
print("Note:At any time press ENTER to continue")
print()
print()
n=input()
print("1) First keep a two digit number in your mind....(Example '23')")
print()
n=input()
print("2) Just add the two digits (Example if 23 then do '2+3=5')")
print()
n=input()
print("3) Subtract this sum from the actual number which you kept.(Example  23-5=18) \n   Now this is your answer")
print()
n=input()
ll=["%^","^&","^*","%%","$%","@#","!@","*#"]
print("Just see the symbol infront of the answer which you got")
n=input()
aa=random.choice(ll)
for i in range(1,10):
    if i%9==0:
        print("",i," : ",aa)
    else:
        print("",i," : ",random.choice(ll))
for i in range(10,100):
    if i%9==0:
        print(i," : ",aa)
    else:
        print(i," : ",random.choice(ll))
print("100",": ",random.choice(ll))

with open('answer','w') as f:
    f.write(aa)
n=input("Press ENTER to check your answer")
print(aa," is the symbol")
print()



