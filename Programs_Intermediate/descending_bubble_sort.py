l = [(1,"rohan verma",3005),(2,"soham guha",5004),(3,"mayhul jindal",7004),(4,'prerit rana',1001)]
dict_1 = {}
for index in range(0,len(l)):
    group = l[index]
    points = group[2]
    dict_1[points] = group
    l[index] = points
    
for passes in range(0,len(l) - 1):
    for index in range(0, len(l) - passes - 1):
        if l[index] < l[index + 1]:
            l[index], l[index + 1] = l[index + 1], l[index]
        else:
            continue
for index_2 in range(0,len(l)):
    element = l[index_2]
    l[index_2] = dict_1[element]
    
print(l)    
            
            