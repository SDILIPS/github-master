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

time_spent = 0
phone_max_time = ''
for entry in calls:
    if int(entry[3]) > time_spent:
        time_spent = int(entry[3])
        phone_max_time = entry[0]

print("{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.".format(telephone_number = phone_max_time, total_time = time_spent))
