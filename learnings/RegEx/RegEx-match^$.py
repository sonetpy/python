# match() method of re module
import re
s1='China is the most populous country in the world'
s2='Most populous country in the world is China'
res=re.match(r'China',s1)
print(res.group()) #prints Match object as China is at the beginning of s2.
res=re.match(r'China',s2)
print(res) #prints None as China is not at the beginning of s2.
if re.search('China',s1) and re.search('China',s2):
# another way to use search() and match()
    print('search possible in s1 and s2')

# like in UNIX we use "^" to search a word at the begining of the line.

'''		abhinav@Ubuntu:~$ ls -l |grep ^d
		drwxr-xr-x 2 abhinav abhinav 4096 Mar 27 12:48 Desktop
		drwxr-xr-x 2 abhinav abhinav 4096 Mar 27 12:48 Documents
		drwxr-xr-x 3 abhinav abhinav 4096 Apr  2 21:31 Downloads
		drwxr-xr-x 2 abhinav abhinav 4096 Mar 27 12:48 Music
		drwxr-xr-x 2 abhinav abhinav 4096 Mar 27 12:48 Pictures
		drwxr-xr-x 2 abhinav abhinav 4096 Mar 27 12:48 Public
		drwxrwxr-x 6 abhinav abhinav 4096 Apr  2 21:41 Python
		drwxr-xr-x 4 abhinav abhinav 4096 Apr  2 00:55 snap
		drwxr-xr-x 2 abhinav abhinav 4096 Mar 27 12:48 Templates
                drwxr-xr-x 2 abhinav abhinav 4096 Mar 30 22:02 Videos
'''

print ("Another way using '^' ")

import re
s1='China is the most populous country in the world'
s2='Most populous country in the world is China'
res=re.search(r'^China',s1)
print(res.group()) #prints Match object as China is at the beginning of the s2.
#res=re.search(r'^China',s2)
#print(res.group()) #prints None as China is not at the beginning of the s2.


# Now we are going to search a word which is at the END of the sentence

import re
s3 = 'Most populous country in the world is China'
res=re.search(r'China$', s3)
print("Using '$China' to find a word last in a Statement :::", res.group())

#### Similarly in UNIX asle we use '$' to find the last word in the statement
'''
$ ls -l | grep Videos$
drwxr-xr-x 2 abhinav abhinav 4096 Mar 30 22:02 Videos
'''

import re
s3='China'
res=re.search(r'^China$', s3)
print ("Combination of ^ @beggning and $ @extreme end of string, matches any word that starts and end. in our example r'^China$'. ::::: ", res.group())
print(res.group())



