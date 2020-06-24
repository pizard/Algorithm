"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
# texts : number, receiving number, Time
# calls : number, receiving number, date, duration(seconds)
# Number
# Default : Start with 0         / (022)40840621
# Mobile : Start with 7,8,9      / 93412 66159
# Telemarketers : Start with 140 / 1402316533
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
"<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016.".
"""


import datetime

def checkMonth(comparison, label):
    return (label == datetime.datetime.strptime(comparison, "%d-%m-%Y %H:%M:%S").strftime("%m-%Y"))

callInformations = {}
for call in calls:
    if checkMonth(call[2], "09-2016"):
        if call[0] not in callInformations.keys():
            callInformations[call[0]] = int(call[3])
        else:
            callInformations[call[0]] += int(call[3])
        if call[1] not in callInformations.keys():
            callInformations[call[1]] = int(call[3])
        else:
            callInformations[call[1]] += int(call[3])

maxDuration = -1
maxPhoneNumber = ""
for phoneNumber, duration in callInformations.items():
    if maxDuration < duration:
        maxPhoneNumber = phoneNumber
        maxDuration = duration

print(maxPhoneNumber," spent the longest time, ", maxDuration, " seconds, on the phone during September 2016.")