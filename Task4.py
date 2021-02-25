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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# set of callers
caller_set = set([x[0] for x in calls])
# set of receivers
receiver_set = set([x[1] for x in calls])
# sysmetric difference
possible_telemarketers = (caller_set.difference(
    receiver_set)).difference(receiver_set)

# set of texters
texter_set = set()
for number in texts:
    texter_set.add(number[0])
    texter_set.add(number[1])


telemarketers_set = possible_telemarketers.difference(
    texter_set)

print("These numbers could be telemarketers: ")
for number in sorted(telemarketers_set):
    print(number)

