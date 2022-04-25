import random as ran
print ("I am thinking of a number between 1 and 20")
guess = input("Take a guess: ")
sec = ran.randint(1,20)
if (int(guess) > sec):
    print ("your guess is high and I guessed it {}".format(sec))
elif (int(guess) < sec):
    print ("your guess is low and I guessed it {}".format(sec))
else :
    print ("You guessed it right")

# Ask the player to guess 6 times.
for i in range(1,7):
    s = ran.randint(1,6)
    g = input("Take a guess")
    if (int(g) > s):
        print("your guess is high and I guessed it {}".format(s))
    elif (int(g) < s):
        print("your guess is low and I guessed it {}".format(s))
    else:
        break
print("You guessed it right")

