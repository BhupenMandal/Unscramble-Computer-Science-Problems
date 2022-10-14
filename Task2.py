"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import pandas as pd

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
df = pd.DataFrame(calls, columns=['In_calls', 'Out_calls', 'Date', 'Time'])
df = df.astype({"Time": int})


df = pd.melt(df, id_vars='Time', value_vars=['In_calls', 'Out_calls'], value_name="Longest_time")
df = df.groupby("Longest_time")[["Time"]].sum()

df = df.sort_values(by="Time", ascending=False)

df = df.reset_index()

number = df['Longest_time'].iat[0]

time = df['Time'].iat[0]

print(f"{number} spent the longest time, {time} seconds, on the phone during September 2016.")
