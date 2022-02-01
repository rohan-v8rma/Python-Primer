import sys

#Standard Input Device

l = sys.stdin.read(5)
print(l)
'''
stdin function is another way of taking input from user
from the standard input device which is keyboard in
most cases. An argument can be given which specifies
the number of bytes that will be assigned or used 
irrespective of how many bytes are entered by the user.
'''

#Standard Output Device

sys.stdout.write('This is the output')

#Standard Error Device

sys.stderr.write('This is the error')