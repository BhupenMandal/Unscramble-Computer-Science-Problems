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

out_calls = []
in_calls = []
out_text = []
in_text = []

for call in calls:
    out_calls.append(call[0])
    in_calls.append(call[1])

for text in texts:
    out_text.append(text[0])
    in_text.append(text[1])

possible_marketers = []

for num in out_calls:
    if (num not in in_calls) and (num not in out_text) and (num not in in_text):
        possible_marketers.append(num)

sorted_possible_marketers = sorted(set(possible_marketers))
print("These numbers could be telemarketers: ")
print(*sorted_possible_marketers, sep="\n")
