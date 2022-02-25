list_1 = [99,65,89,23,29]
length = int(len(list_1))
number_of_passes = length - 1 # length is 5
for passes in range(0,number_of_passes):
    for index in range(0,length - 1):
        if list_1[index] > list_1[index + 1]:
            list_1[index],list_1[index + 1] = list_1[index + 1],list_1[index]
            
        else:
            continue
    length = length -1
print(list_1)    
