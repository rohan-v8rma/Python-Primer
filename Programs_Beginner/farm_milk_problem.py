no_of_farms = int(input("Please enter the the number of farms ---> "))

def milk_amount(no_of_farms):
    flag = 1
    total = 0
    while flag <= no_of_farms:
        print("Data for farm number", flag)
        liters = int(input("Liters? ---> "))
        milliliters = int(input("Milliliters? ---> "))
        total += liters + milliliters/1000
        flag += 1
    return total
print("Total amount of milk collected is",milk_amount(no_of_farms),"liters")
