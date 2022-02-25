num = -1
while num <= 0:
    num = int(input("What is the number? >> "))
def no_of_digits(num):
    quotient = 0 
    no_of_digits = 0
    while quotient == 0:
        quotient = num // 10 ** no_of_digits
        if quotient >= 10:
            quotient = 0
        else:
            return (no_of_digits + 1)
        no_of_digits += 1

def finding_x_place_digit(num, place):
    digitsAmount = no_of_digits(num)
    x_place_digit = (num - (num // 10 ** place) * 10 ** place - num % ((num // 10 ** (place - 1)) * 10 ** (place - 1)))// 10 ** (place - 1) 
    return x_place_digit

def combinations(num):
    digitsAmount = no_of_digits(num)
    for first_place_selected in range(digitsAmount, 0, -1):
        first_digit = finding_x_place_digit(num, first_place_selected)
        for second_place_selected in range(first_place_selected - 1, 0, -1):
            second_digit = finding_x_place_digit(num, second_place_selected)
            print(first_digit * 10 + second_digit, second_digit * 10 + first_digit)
if num < 10:
    print(num)
else:
    combinations(num)