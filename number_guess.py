import random

toprange=input("Type a number:")

if toprange.isdigit():
    toprange=int(toprange)
    if toprange<=0:
        print("Please type a number larger than zero")
        quit()
else:
    print("Please type a number")
    quit()

random_number=random.randint(0,toprange)
while True:
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number")
        continue
    if user_guess==random_number:
        print("You got it :)")
        break
    else:
        print("You got in wrong :()")