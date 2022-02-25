n = 1 
t = int(input("till what natural number should both the sums be calculated?"))
sum_of_even = sum_of_odd = 0
while (n < t + 1):
    if (n%2):
        sum_of_even += n
    else:
        sum_of_odd += n
    n = n + 1
print ("Sum of even natural numbers =",sum_of_even)
print ("Sum of odd natural numbers =",sum_of_odd)    
        

