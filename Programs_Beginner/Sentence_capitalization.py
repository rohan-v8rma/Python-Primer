string = str(input("what is the sentence"))
t = string.split()
number_of_terms = len(t)
a = 0
for i in range(0, number_of_terms):
    t[i].capitalize()

capitalized_string = t.join()   
print(capitalized_string)    
