'''
with open("spam.txt", mode='w') as myfile:
    myfile.write('\nThe spam van')
    myfile.write('\nSales log')
myfile.close()
'''
#OR
sales_log = open('spam_order.txt', 'w')
sales_log.write('The spam van\n')
sales_log.write('Sales log\n')
sales_log.close()
#If the file doesn’t exist for a write or an append, Python will automatically create the file.

