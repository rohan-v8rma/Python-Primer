a = int(input("what is the number"))
a = str(a)
a = a.strip()
i = 0
b = 0
while i<len(a):
    b += int(a[i])*(10**(i))
    i += 1
print(b)    
