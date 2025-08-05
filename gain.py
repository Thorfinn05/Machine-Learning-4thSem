import csv
import pandas as pd

data = pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\Weather.csv")
print(data)
Sunny = len(data[data['Outlook'] == 'Sunny'])
Sunny_Y = len(data[(data['Outlook'] == 'Sunny') & (data['Play Tennis'] == 'Yes')])
Sunny_N = len(data[(data['Outlook'] == 'Sunny') & (data['Play Tennis'] == 'No')])

print(Sunny, Sunny_Y, Sunny_N)