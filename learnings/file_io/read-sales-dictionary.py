menu = open('menu.txt', 'r')
print(menu.read())
menu.close()
# Reading an individual line from a file
menu = open('menu.txt', 'r')
print('1st line:', menu.readline())
print('2nd Line:' , menu.readline())
menu.close()
#Reading the menu as a list of lines
new_menu = []
menu = open('menu.txt', 'r')
for lines in menu:
    lines = lines.strip() #str.strip() removes any leading or trailing whitespace.
    new_menu.append(lines)
print("list")
print (new_menu)
menu.close()


