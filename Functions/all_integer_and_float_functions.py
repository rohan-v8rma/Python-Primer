'''All integer and float function

                                            INDEX
    1. Restricting Calculation to Certain Amount of Decimals
    2. Taking input of complex number
    -. Arithmetic Underflow/Overflow -- non existent in today's systems
'''
import math

'''1. Restricting Calculation to Certain Amount of Decimals'''

#(i) round function
a = 5.7664
print(round(a, 2))
#this number will be rounded to 2 decimal places
#in this case rounding is done

#(ii) truncate
print(math.trunc(a * 100)/100)
#this will display value of 'a' to 2 decimal places
#no rounding will occur in this case

#(ii) format function of python
a_float = 3.14159
formatted_a = format(a_float, '.2f')
#Format the float with two decimal places
print(formatted_a)


'''2. Taking input of/Defining a complex number'''

complex_num = complex(input("Enter a complex number >> "))
print(complex_num.real)
print(complex_num.imag)
#OR
real_part = 10
imaginary_part = 23
complex_num0 = complex(real_part, imaginary_part)
print(complex_num0)


