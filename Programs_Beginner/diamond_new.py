size = int(input("Enter size?"))

if size > 5:
    size = size
else:
    size = 5    
if size % 2 == 0:
    size += 1
else:
    size = size      
for i in range(1,int((size + 1)/2) + 1):
    if i == 1:
        print (" "*int((size - 1 )/2),"*",sep = "")
    else:
        print(" "*int((size + 1)/2 - i ),"*"," "*((i - 1) * 2 - 1 ),"*",sep = "")
        
for t in range(int((size + 1)/2),1,-1):      
    if t == 2:
        print (" "*int((size - 1 )/2),"*",sep = "")
    else:
        print(" "*int((size + 3)/2 - t),"*"," "*(t * 2 - 5 ),"*",sep = "")
                        
        
        
    
















"""
  *
 * *
*   *
 * *
  *
   *  
  * *
 *   *
*     *
 *   *
  * *
   *  
"""
 