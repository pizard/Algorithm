"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

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

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)



list.sort(calls)
"""
texts : number, receiving number, Time
calls : number, receiving number, date, duration(seconds)
Number
Default : Start with 0         / (022)40840621
Mobile : Start with 7,8,9      / 93412 66159
Telemarketers : Start with 140 / 1402316533
"""


# 1. never send or receive texts
# 2. never receive incoming calls


telemarketers = []
nonTelemarketers = []

for text in texts:
    if text[0][:3] == "140":
        nonTelemarketers.append(text[0])
    if text[1][:3] == "140":
        nonTelemarketers.append(text[0])

for call in calls:
    if call[1][:3] == "140":
        if call not in nonTelemarketers:
            if call in telemarketers:
                nonTelemarketers.append(call[1])

    if call[0][:3] == "140":
        if call in nonTelemarketers:
            if call in telemarketers:
                telemarketers.remove(call[0])
        elif call not in telemarketers:
            telemarketers.append(call[0])

for telemarketer in telemarketers:
    print(telemarketer)