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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

codes_area = []

for i in calls:
    out_calls = (i[0])
    in_calls = (i[1])

    if out_calls.startswith('(080)'):
        if in_calls.startswith('('):
            first = 1
            last = in_calls.find(')')
            codes_area.append(in_calls[first:last])

        elif in_calls.startswith('7') or in_calls.startswith('8') or in_calls.startswith('9'):
            codes_area.append(in_calls[0:4])

        elif in_calls.startswith('140'):
            codes_area.append('140')

list_area_codes = []
sorted_codes_area = sorted(set(codes_area))
for codes in sorted_codes_area:
    list_area_codes.append(codes)


print(f"The numbers called by people in Bangalore have area codes:")
print(*list_area_codes, sep='\n')

count = codes_area.count('080')
total = len(codes_area)
percent = (count / total) * 100

print(f"\n{round(percent, 2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in "
      f"Bangalore.")
