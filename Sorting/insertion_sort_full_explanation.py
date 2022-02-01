list_1 = [76,85,34,23,65,12,9]
for index in range(1,len(list_1)):
    element_to_be_sorted = list_1[index]
    comparison_index = index - 1
    '''we have to compare an element with the one on its left thus comparison
    element is at one index less than the element to be sorted initially
    ''' 
    while comparison_index >= 0 and element_to_be_sorted < list_1[comparison_index]:
        ''' the condition above is kept because if the comparison element index
        is less than 0, then there are now other elements left to compare with. 
        And the second condition is kept because for the right shift of 
        comparison element,it is mandatory that the element to be sorted 
        is smaller than the comparison element'''
        list_1[comparison_index + 1] = list_1[comparison_index]
        '''This command right shifts the comparison element when it is
        greater than the element to be sorted'''
        comparison_index = comparison_index - 1 
    else:
        '''This else statement is processed while exiting the while loop and 
        the while loop is exited when either, there are no other elements 
        left to compare, {comparison = -1} so the element to be sorted is 
        placed at index (comparison + 1) which is 0 i.e., at the start of 
        the list. The other case is when the element to be sorted is 
        greater than the comparison element in which case it is placed at 
        an index to the right of it (comparison + 1)'''
        list_1[comparison_index + 1] = element_to_be_sorted
        
        
                
                            
            