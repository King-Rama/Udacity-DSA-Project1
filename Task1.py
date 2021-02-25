"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

my_set = set()
for (x,y) in zip(calls, texts):
    my_set.add(x[0])
    my_set.add(x[1])
    my_set.add(y[0])
    my_set.add(y[1])

print("There are {} different telephone numbers in the records.".format (len(my_set)))

