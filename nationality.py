import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\Nationality.csv")
print(data)
d = { 'UK':0, 'USA':1, 'N':2 }
data['Nationality'] = data['Nationality'].map(d)
d = { 'YES':1, 'NO':0 }
data['Go'] = data['Go'].map(d)
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = data[features]
Y = data['Go']
dtree = DecisionTreeClassifier()
dtree.fit(X,Y)
plt.figure(figsize=(10,6))
tree.plot_tree(dtree, feature_names=features, filled = True)
plt.show()