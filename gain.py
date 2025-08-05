import csv
import pandas as pd

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