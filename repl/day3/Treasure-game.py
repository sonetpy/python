print("Welcome to Treasure Island. Your Mission is to find the treasure")
direction = input("Left or Right? ")
if direction == 'Right':
    print("game over!")
elif direction == 'Left':
    sw = input("Would like to swim or wait: ")
    if sw == 'swim':
        print('game over!')
    elif sw == 'wait':
        door = input("Which door Red, Blue or Yellow: ")
        if door == 'yellow':
            print('you win!')
        else:
            print('game over')
    else:
        print("game over!")
else:
    print("game over dude!")
