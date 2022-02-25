a = int(input("what is the number"))
b = 0
for i in range(1,a):
        if a%i == 0:
            b += i
        else:
            continue
if a == b:
    print("the number is perfect")
else:
    print("the number is not perfect")    
