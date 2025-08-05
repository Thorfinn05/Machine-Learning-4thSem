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

entropy_total = entropy(total_yes, total_no)

# 7. Entropy for each Outlook category
entropy_sunny = entropy(Sunny_Y, Sunny_N)
entropy_rainy = entropy(Rainy_Y, Rainy_N)
entropy_overcast = entropy(Overcast_Y, Overcast_N)

# 8. Weighted entropy for Outlook attribute
weighted_entropy = ((Sunny / total) * entropy_sunny +
                    (Rainy / total) * entropy_rainy +
                    (Overcast / total) * entropy_overcast)

# 9. Information Gain for Outlook
gainn_outlook = entropy_total - weighted_entropy

# 10. Print results
print("Entropy (total):", round(entropy_total, 4))
print("Entropy (Sunny):", round(entropy_sunny, 4))
print("Entropy (Rainy):", round(entropy_rainy, 4))
print("Entropy (Overcast):", round(entropy_overcast, 4))
print("Information Gain (Outlook):", round(gainn_outlook, 4))
print('\n\n')

def calc_gain(attribute):
    categories = data[attribute].unique()
    weighted_entropy = 0
    for cat in categories:
        subset = data[data[attribute] == cat]
        pos = len(subset[subset['Play Tennis'] == 'Yes'])
        neg = len(subset[subset['Play Tennis'] == 'No'])
        ent = entropy(pos, neg)
        weight = len(subset) / total
        weighted_entropy += weight * ent
    gain = entropy_total - weighted_entropy
    return round(gain, 4)

# 6. Calculate information gain for each attribute
gain_outlook = calc_gain('Outlook')
gain_humidity = calc_gain('Humidity')
gain_wind = calc_gain('Wind')
gain_temperature = calc_gain('Temperature')

# 7. Print information gains
print("Information Gain (Outlook):", gain_outlook)
print("Information Gain (Humidity):", gain_humidity)
print("Information Gain (Wind):", gain_wind)
print("Information Gain (Temperature):", gain_temperature)

# 8. Determine root node (attribute with highest info gain)
gains = {
    'Outlook': gain_outlook,
    'Humidity': gain_humidity,
    'Wind': gain_wind,
    'Temperature': gain_temperature
}
root_node = max(gains, key=gains.get)

print("\nRoot Node of the Decision Tree:", root_node)
