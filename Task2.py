"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

my_set = set()
for (x, y) in zip(calls, texts):
    my_set.add(x[0])
    my_set.add(x[1])
    my_set.add(y[0])
    my_set.add(y[1])


# creating a dict to hold phone numbers as value and time_spent as keys
my_dict = {x: 0 for x in my_set}
for x in calls:
    my_dict[x[0]] = my_dict.get(x[0]) + int(x[-1])  # caller
    my_dict[x[1]] = my_dict.get(x[1]) + int(x[-1])  # receiver

# getting the longest item after sorting the tuple keys as integers

maxima = max(my_dict, key=my_dict.get)

print(
    "{} spent the longest time, {} seconds, on the phone during September 2016.".format (maxima, my_dict[maxima]))
