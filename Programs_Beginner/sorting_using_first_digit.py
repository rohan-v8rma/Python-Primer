list_1 = [387,410,285,106]
dict_1 = {}
for index in range(0,len(list_1)):
    number = str(list_1[index])
    first_digit = int(number[-1])
    dict_1[first_digit] = int(number)
    list_1[index] = first_digit
    
for index_2 in range(1,len(list_1)):
    element_to_be_sorted = list_1[index_2]
    comparison_index = index_2 - 1 
    while comparison_index >= 0 and element_to_be_sorted < list_1[comparison_index]:
        list_1[comparison_index + 1] = list_1[comparison_index]
        comparison_index = comparison_index - 1
    else:
        list_1[comparison_index + 1] = element_to_be_sorted

for index_3 in range(0,len(list_1)):
    list_1[index_3] = dict_1[list_1[index_3]]
    
print(list_1)    