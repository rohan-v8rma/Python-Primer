import csv

'''CSV Reader'''

file = open(r'C:\Users\Rohan Verma\Dropbox\Computer_code\Example.csv', 'r')
myreader = csv.reader(file, delimiter = ',')
for row in myreader:
    print(row)
file.close()

'''CSV Writer'''

file1 = open(r"C:\Users\Rohan Verma\Dropbox\Computer_code\Example.csv", 'a', newline = '')
#If newline='' is not specified, newlines embedded inside quoted 
# fields will not be interpreted correctly, and on platforms such 
# as Windows that use \r\n linendings on write an extra \r will 
# be added. It should always be safe to specify newline='', since 
# the csv module does its own (universal) newline handling.

writer = csv.writer(file1)
inputs = int(input('How many entries?'))
for i in range(inputs):
    list = eval(input('list?'))
    writer.writerow(list)
file1.close()



