# Code to read-write the content of the file
my_content=['This is using loop-iteration-1','This is using loop iteration-2','This is using loop iteration-3']
fo = open('with_loop.txt','w')
for each_line in my_content:
    fo.write(each_line+'\n')
fo.close()
fo = open('with_loop.txt','r')
print(fo.read()+'\n')
### Below code will append the data
my_content=['This is using loop-iteration-4','This is using loop iteration-5','This is using loop iteration-6']
fo = open('with_loop.txt','a')
for each_line in my_content:
    fo.write(each_line+'\n')
fo.close()
fo = open('with_loop.txt','r')
print(fo.read())

print("\nI want to read last 2 lines now")
fo = open('with_loop.txt','r')
data = fo.readlines()
fo.close()
print(data[2:5])

