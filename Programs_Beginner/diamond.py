size = int(input("what is size"))\
       
if (size >= 5):
    
    if size % 2 == 0:
                     size = size + 1
    elif size %2 != 0:
                     size = size

    for t in range(1 , int((size + 1)/2) + 1): 
        for i in range(1 , int((size + 1)/2) - t + 1 ):
             print ("", end = " ")
        for k in range(1 , 2):
            if (t == 1):
                 print("*")
            else:
                 print("* "," "*(2*(t-2)),"*", sep = "") 
    for l in range(int((size + 1)/2) - 1, 0, -1):
        for m in range(1, int((size + 1)/2) - l + 1):
            print("", end = " ")
        for n in range(1, 2):
            if (l == 1):
                 print("*")
            else:
                 print("* "," "*(2*(l - 2)),"*", sep = "") 
         
else:
    print("Invalid Size")
"""
  *
 * *
*   *
 * *
  *
"""
               
