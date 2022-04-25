row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

position1 = int(input("where do you want to position? "))
position2 = int(input("where do you want to position? "))
map1 = [row1, row2, row3]
map1[position1][position2] = "X"

print(f"{row1}\n{row2}\n{row3}")
