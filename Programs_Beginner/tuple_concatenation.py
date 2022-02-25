a = eval(input("first tuple?"))
b = eval(input("second tuple"))
a = list(a)
b = list(b)
c = []
d = len(a) + len(b)
for i in range(0,len(a)):
    c.append(a[i])
for i in range(0,len(b)):
    c.append(b[i])
print(tuple(c))    
    
