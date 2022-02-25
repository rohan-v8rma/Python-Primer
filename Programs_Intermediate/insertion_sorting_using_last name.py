L = [("rohan verma","physics",100),("soham guha","chemistry",101),("mayhul jindal","maths", 102)]
dictionary = {}
for index in range(0,len(L)):
    group = L[index]
    name = group[0].split()
    last_name = name[-1]
    dictionary[last_name] = L[index]
    L[index] = last_name
for index_2 in range(1,len(L)):
    element_to_be_sorted = L[index_2]
    comparison_index = index_2 - 1
    while comparison_index >= 0 and element_to_be_sorted < L[comparison_index]:
        L[comparison_index + 1] = L[comparison_index]
        comparison_index -= 1
    else:
        L[comparison_index + 1] = element_to_be_sorted
        
for index_3 in range(0,len(L)):
    L[index_3] = dictionary[L[index_3]]

print(L)    