number_of_lines = int(input("how many lines"))
for line_number in range(1, number_of_lines + 1):
    for space_number in range(1, number_of_lines - line_number+1):
        print(" ", end = '')
    for star_number in range(1, line_number+1):
        print("* ", end = "")
    print("\n")    
    
    