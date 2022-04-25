#!/usr/bin/python3.9
#Create a database in the following format

#	Interface		IP			status
	
#1	Ethernet0		1.1.1.1			up
#2	Ethernet1		2.2.2.2			down
#3	Serial0			3.3.3.3			up
#4	Serial1			4.4.4.4			up

# Write a python program to find status of a given interface
interface = ['Ethernet0', 'Ethernet1', 'Serial0', 'Serial1']
ip = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']
status = ['up', 'down', 'up', 'up']

#db = {'1': ['Ethernet0', '1.1.1.1', 'up'], '2': ['Ethernet1', '2.2.2.2', 'down'], '3': ['Serial0', '3.3.3.3', 'up'], '4': ['Serial1', '4.4.4.4', 'up']}
#How to iterate over 2+ lists at the same time
db = zip(interface, ip, status)
print (db)
print (" \t\t\tInterface\t\t\tIP\t\t\tStatus")
k = 0
for interface, ip, status in db:
    k = k + 1
    print ("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(k, interface, ip, status))

