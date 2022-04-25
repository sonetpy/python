slang = {'cheerio':'goodbye', 'knackered':'tired', 'smashing':'terrific'}
print (slang)
#Trying to access a key that doesn’t exist will cause an error.
#print(slang['bloody'])
print("\nIf you want to check if a word is in the dictionery, use get ()")
print("\nUsing get() is a best practicse as it will not crash your program")
result = slang.get('bloody')
print(result)
#Enhancing a program a bit
if result:
    print(result)
else:
    print("key doesn't exsist")


        
