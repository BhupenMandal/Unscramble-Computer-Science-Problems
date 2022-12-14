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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
first_record_texts = texts[0]
print(f"First record of texts, {first_record_texts[0]} texts {first_record_texts[1]} at the time"
      f"{first_record_texts[2][10:]}")
last_record_calls = calls[-1]
print(f"Last record of calls, {last_record_calls[0]} calls {last_record_calls[1]} at the time"
      f"{last_record_calls[2][10:]}, lasting {last_record_calls[3]} seconds")
