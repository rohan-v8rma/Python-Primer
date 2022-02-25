for a in range (1,6):
    number = int(input("Guess the number?\n"))
    if (10<=number<=50):
        if (number == 37):
            print("Correct!!!!!!")
        else: 
            print("Try again!")   
    else:
        print("Why so wrong input????") 
        break
print("End of game :)") 