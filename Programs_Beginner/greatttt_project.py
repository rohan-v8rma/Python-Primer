import time 
t = 0.04
i = 2
while i > 0:
    if i % 2 == 0:
        for l in range(20,66):
            print("8",'='*l,'D',sep = '')
            time.sleep(t)
        i += 1
        continue
    elif i % 2 != 0:
        for m in range(64,20,-1):
            print("8",'='*m,'D',sep = '')
            time.sleep(t)
        i += 1
        
        continue     
