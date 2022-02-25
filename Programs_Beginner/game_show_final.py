a = 0 
import random
while a<6:
    number = random.randint(10,50)
    guess = int(input("guess?\n"))
    if guess == number:
        print("correct! you won!")
        break
    elif (10<=guess<=50) and (guess != number):
        print("the number was",number)
        print("try again")
    else:
        print("why so wrong input")
        break
print("end of game")        