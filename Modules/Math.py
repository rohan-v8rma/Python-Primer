'''Math Module'''

import math

arg = 2
base = 2
exp = 3
num = 25
b = 6
l1 = [5,4]

print(math.trunc(12.04))
#this function returns only the integer part of the function
print(math.trunc(154.958327 * 100)/100)
#in this way, the answer can be restricted to only 2 decimal places (NOT ROUNDED)

print(math.ceil(1.03))
#returns the least integer value higher than the given number

print(math.floor(1.51))
#returns the greatest integer value lower than the given number

print(math.exp(arg))
#returns (e^argument)

print(math.fabs(-1))
#this function returns the value in 'float' data type
#OR
print(abs(-1))
#returns modulus of given argument

print (math.pow(base,exp))
#returns base^exp

print(math.radians(360))
#converts degrees to radians

print(math.degrees(4)) 
#converts radians to degrees

print(math.log(num, b))
#returns log of num to the base b




