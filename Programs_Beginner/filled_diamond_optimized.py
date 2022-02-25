size = int(input("Enter size?"))
#size refers to number of lines in diamond as well as width of longest line 
# in middle of diamond
while size < 3 or size % 2 == 0:
    size = int(input("Enter size? only odd number greater than or equal to 3"))
for no_of_stars_inc in range(1, int((size + 1)/2) + 1):
    print ((("* "*(no_of_stars_inc - 1)) + "*").center(size,' '))
for no_of_stars_dec in range(int((size + 1)/2) - 1, 0, -1):      
    print((("* "*(no_of_stars_dec - 1)) + '*').center(size,' '))
        