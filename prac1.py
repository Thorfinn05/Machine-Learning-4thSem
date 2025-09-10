import numpy as np
import pandas as pd
import csv
import math

data = pd.read_csv("Weather-D.csv")
print(data)

total_yes = len(data[data["Play Football"] == "Yes"])
total_nos = len(data[data["Play Football"] == "No"])
total = total_yes + total_nos
print(total, total_yes, total_nos)

def entropy(pos, neg):
    total = pos + neg
    if total == 0 or pos == 0 or neg == 0:
        return 0
    p_pos = pos/total
    p_neg = neg/total
    return -p_pos * math.log2(p_pos) - p_neg * math.log2(p_neg)

entropy_total = entropy(total_yes, total_nos)
print(entropy_total)

def calc_gain(attribute):
    categories = data[attribute].unique()
    weighted_entropy = 0
    for cat in categories:
        subset = data[data[attribute] == cat]
        pos = len(subset[subset["Play Football"] == "Yes"])
        neg = len(subset[subset["Play Football"] == "No"])
        ent = entropy(pos, neg)
        weight = len(subset)/total
        weighted_entropy += weight * ent
    gain = entropy_total - weighted_entropy
    return round(gain, 4)

gain_outlook  = calc_gain("Outlook")
gain_windy = calc_gain("Windy")
gain_humidity = calc_gain("Humidity")
gain_temperature = calc_gain("Temperature")
print(gain_outlook, gain_temperature, gain_windy, gain_humidity)

gains = {
    'Outlook': gain_outlook,
    'Temperature': gain_temperature,
    'Windy': gain_windy,
    'Humidity': gain_humidity
}
print(gains)

root_node = max(gains, key=gains.get)
print(root_node)