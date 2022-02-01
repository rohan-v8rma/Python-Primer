a = 20
b = 0
try:
    print(a / b)
#the error mentioned after except is the case in which except block is executed
except ZeroDivisionError:
    print('There is divide by zero error')
finally:
    print('This is going to be executed no matter what')