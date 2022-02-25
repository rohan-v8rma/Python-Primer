Str_1 = str(input("what is first string?"))
Str_2 = str(input("what is second string?"))
print(Str_2)
a = 0
b = 3 + 6 * int((len(Str_1)/2) - 1)
c = -1
d = 0
for t in range(0, int(((len(Str_1)) + 1)/2)):    
    if (len(Str_1))%2 == 0:
        print(d*" ",Str_1[a]," "*b,Str_1[c], sep = '')
        a = a + 1
        b = b - 6
        c = c - 1
        d = d + 3
    elif (len(Str_1))%2 != 0:
        if t == int((len(Str_1) + 1)/2) - 1:
            print(((int((len(Str_1) - 1)/2) * 3) - 1)*" ",Str_1[t])
        else:    
            print(d*" ",Str_1[a]," "*b,Str_1[c], sep = '')
            a = a + 1
            b = b - 6
            c = c - 1
            d = d + 3
        
"""
P               n
   y         o
      t   h
                 
b   b      
  p
2 5 8 11 14
3 5 7 9  11
"""    