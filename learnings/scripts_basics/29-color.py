'''
Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}

'''

color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]
colorlist = color_list_1 + color_list_2
print (colorlist)
k = set (colorlist)
print (k)

z = []

for i in color_list_1:

    for j in color_list_2:

        if (color_list_1[i] != color_list_2[j]):

            z = color_list_1[i]
print (z)

