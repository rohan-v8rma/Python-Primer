a = int(input("what is bigger number?"))
b = int(input("what is smaller number?"))
if (b > a):
    a = b;b = a
    if (b % a == 0):
        print("the bigger number is divisible by smaller number")    
    elif (b % a > 0) or (b % a < 0):
        print("the bigger number is not divisible by smaller number")
    else:
        print("invalid input")        
elif (a % b == 0):
    print("the bigger number is divisible by smaller number")    
elif (a % b > 0) or (a % b < 0):
    print("the bigger number is not divisible by smaller number")    
else:
    print("invalid input")     
