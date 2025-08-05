import csv
import pandas as pd
import math

data = pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\Weather.csv")
print(data)

Sunny = len(data[data['Outlook'] == 'Sunny'])
Sunny_Y = len(data[(data['Outlook'] == 'Sunny') & (data['Play Tennis'] == 'Yes')])
Sunny_N = len(data[(data['Outlook'] == 'Sunny') & (data['Play Tennis'] == 'No')])
print("Sunny: ", Sunny, " ", "Sunny_Y: ", Sunny_Y, " ", "Sunny_N: ", Sunny_N)

Overcast = len(data[data['Outlook'] == 'Overcast'])
Overcast_Y = len(data[(data['Outlook'] == 'Overcast') & (data['Play Tennis'] == 'Yes')])
Overcast_N = len(data[(data['Outlook'] == 'Overcast') & (data['Play Tennis'] == 'No')])
print("Overcast: ", Overcast, " ", "Overcast_Y: ", Overcast_Y, " ", "Overcast_N: ", Overcast_N)

Rainy = len(data[data['Outlook'] == 'Rainy'])
Rainy_Y = len(data[(data['Outlook'] == 'Rainy') & (data['Play Tennis'] == 'Yes')])
Rainy_N = len(data[(data['Outlook'] == 'Rainy') & (data['Play Tennis'] == 'No')])
print("Rainy: ", Rainy, " ", "Rainy_Y: ", Rainy_Y, " ", "Rainy_N: ", Rainy_N)

total_yes = len(data[data['Play Tennis'] == 'Yes'])
total_no = len(data[data['Play Tennis'] == 'No'])
total = total_yes + total_no

def entropy(pos, neg):
    total = pos + neg
    if total == 0 or pos == 0 or neg == 0:
        return 0
    p_pos = pos/total
    p_neg = neg/total
    return -p_pos * math.log2(p_pos) - p_neg * math.log2(p_neg)

