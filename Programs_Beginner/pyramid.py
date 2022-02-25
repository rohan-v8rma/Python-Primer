#printing a pyramid
#number_of_lines = number of stars on base?number of lines
number_of_lines = int(input("Enter the number of lines in triangle?"))
for line_number in range (1, number_of_lines + 1):
    for star_number in range (1, line_number + 1):
        print("*", end="")
    print('\n')