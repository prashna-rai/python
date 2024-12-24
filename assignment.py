# Program to determine division based on marks percentage


# marks_percentage = int(input("Enter your marks percentage: "))
# if marks_percentage >= 60:
#     print("First Division")
# elif marks_percentage >=50:
#     print("Second Division")
# elif marks_percentage >= 35:
#     print("Third Division")
# else:
#     print("Fail")

    
# algorithm
# step1=Start 
# step2=Generate a random number 1 to 100
# step3=prompt the player to guess the number.
# step4= Compare the player's guess with the random number:
# If the guess is too high, inform the player and allow another guess.
# If the guess is too low, inform the player and allow another guess.
# If the guess is correct, congratulate the player .
# step5=End the game


import random
random_number = random.randint(1, 100)
a = 1
while a<=5:

    guess_number = int(input("Guess any number "))    
    if guess_number == random_number:
        print("congratulation!!! your gueses correct,")
        break

    if guess_number<random_number:
        print("your guess is less than random number ")
    else:
        print("your guess is greater than random number ")

