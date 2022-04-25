# Use dict as values
marks2= {'jose' : {'maths': 85 , 'english': 90, 'science' : 95} , 'peter' : {'marks': 80 , 'english':85 , 'science': 90}}
print ("Marks of Jose in Science :", marks2['jose']['science'])

marks2['jose']['science'] = 86
print ("Marks of Jose is now changed for Science :", marks2['jose']['science'])

print (marks2)
