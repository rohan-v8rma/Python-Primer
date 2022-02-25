size = 0 
while size < 3 or size % 2 == 0:
    size = int(input("Enter size?only odd number more than or equal to 3"))
for i in range(1,int((size + 1)/2) + 1):
    print(" "*int((size + 1)/2 - i ) + "*" + " *"*(i - 1))       
for t in range(int((size - 1)/2),0,-1):      
    print(" "*int((size + 1)/2 - t) + "*" + " *"*(t - 1))
                        
        