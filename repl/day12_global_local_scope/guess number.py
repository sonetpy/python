import random
stage = input("you want easy or hard :")
number = random.randint(1, 100)

if stage == 'easy':
    count = 10
    for i in range(10):
        #print (f"you have {count} attempts left")
        guess = int(input("enter a number to guess: "))
        if guess == number:
            print(f"wow! you guessed it dude in {count} attempts only")
            exit()
        elif guess > number:
            print("your guessed number is high")
        elif guess < number:
            print("your guessed number is low")

        count -= 1
        print(f"you have {count} attempts left")

    else:
        print("Sorry! try again")

if stage == 'hard':
    count = 5
    for i in range(5):
        #print (f"you have {count} attempts left")
        guess = int(input("enter a number to guess: "))
        if guess == number:
            print(f"wow! you guessed it dude in {count} attempts only")
            exit()
        elif guess > number:
            print("your guessed number is high")
        elif guess < number:
            print("your guessed number is low")

        count -= 1
        print(f"you have {count} attempts left")

    else:
        print("Sorry! try again")







