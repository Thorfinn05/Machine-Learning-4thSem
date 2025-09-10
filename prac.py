import numpy as np
import pandas as pd
import csv
import math

data = pd.read_csv("Weather-D.csv")
print(data)

Sunny = len(data[data["Outlook"] == "Sunny" ])
Sunny_Y = len(data[(data["Outlook"] == "Sunny") & (data["Play Football"] == "Yes")])
Sunny_N = len(data[(data["Outlook"] == "Sunny") & (data["Play Football"] == "No")])
print("Sunny: ",Sunny, "Sunny_Y: ", Sunny_Y, "Sunny_N: ", Sunny_N)

Overcast = len(data[data['Outlook'] == 'Overcast'])
Overcast_Y = len(data[(data['Outlook'] == 'Overcast') & (data['Play Football'] == 'Yes')])
Overcast_N = len(data[(data['Outlook'] == 'Overcast') & (data['Play Football'] == 'No')])
print("Overcast: ", Overcast, " ", "Overcast_Y: ", Overcast_Y, " ", "Overcast_N: ", Overcast_N)

Rainy = len(data[data['Outlook'] == 'Rainy'])
Rainy_Y = len(data[(data['Outlook'] == 'Rainy') & (data['Play Football'] == 'Yes')])
Rainy_N = len(data[(data['Outlook'] == 'Rainy') & (data['Play Football'] == 'No')])
print("Rainy: ", Rainy, " ", "Rainy_Y: ", Rainy_Y, " ", "Rainy_N: ", Rainy_N)

total_yes = len(data[data["Play Football"] == "Yes"])
total_no = len(data[data["Play Football"] == "No"])
total = total_yes + total_no

def entropy(pos, neg):
    total = pos + neg
    if total == 0 or pos == 0 or neg == 0:
        return 0
    p_pos = pos/total
    p_neg = neg/total
    return -p_pos * math.log2(p_pos) - p_neg * math.log2(p_neg)

entropy_total = entropy(total_yes, total_no)
print(entropy_total)

entropy_sunny = entropy(Sunny_Y, Sunny_N)
print(entropy_sunny)
entropy_overcast = entropy(Overcast_Y, Overcast_N)
print(entropy_overcast)
entropy_rainy = entropy(Rainy_Y, Rainy_N)
print(entropy_rainy)

weight_sunny = Sunny/total
weight_rainy = Rainy/total
weight_overcast = Overcast/total
print(weight_sunny, weight_overcast, weight_rainy)

weighted_entropy_outlook = (weight_sunny * entropy_sunny) + (weight_overcast * entropy_overcast) + (weight_rainy * entropy_rainy)
print(weighted_entropy_outlook)

gain_outlook = entropy_total - weighted_entropy_outlook
print(gain_outlook)