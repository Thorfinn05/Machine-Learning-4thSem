import math
from collections import Counter
import pandas as pd

# Step 1: Define Euclidean distance
def distance(p1, p2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

# Step 2: Define KNN function
def knn(train_data, test_point, k=3):
    distances = []
    for features, label in train_data:
        d = distance(features, test_point)
        distances.append((d, label))
    # Sort by distance
    distances.sort(key=lambda x: x[0])
    # Pick k nearest
    k_nearest = distances[:k]
    # Extract labels
    labels = [label for _, label in k_nearest]
    # Get most common label
    most_common = Counter(labels).most_common(1)[0][0]
    return most_common

# Step 3: Load data from CSV
# Example CSV content (data3.csv):
# feature1,feature2,label
# 1,2,ClassA
# 2,3,ClassA
# 3,3,ClassA
# 6,8,ClassB
# 7,7,ClassB
# 8,9,ClassB

df = pd.read_csv('D:\Github\Machine-Learning-4thSem\PCA2\data3.csv')
print("Training DataFrame:\n", df, "\n")

# Step 4: Convert dataframe into (features, label) tuples
train_data = [([row.feature1, row.feature2], row.label) for _, row in df.iterrows()]
print("Processed Training Data:\n", train_data, "\n")

# Step 5: Test a single point
test_point = [5, 5]
predicted_class = knn(train_data, test_point, k=3)
print(f"Test Point: {test_point} -> Predicted Class: {predicted_class}\n")

# Step 6: Test on multiple data points
# test_data = [
#     ([1.5, 2.0], "ClassA"),
#     ([2.5, 3.0], "ClassA"),
#     ([7.0, 8.0], "ClassB"),
#     ([5.0, 5.0], "ClassA"),
#     ([6.5, 6.5], "ClassB"),  # corrected label (was ClassA before)
# ]

# errors = 0
# for features, true_label in test_data:
#     pred = knn(train_data, features, k=3)
#     print(f"Point {features} -> Predicted: {pred}, Actual: {true_label}")
#     if pred != true_label:
#         errors += 1

test_df = pd.read_csv('D:\Github\Machine-Learning-4thSem\PCA2\data4.csv')
print("Test Data:\n", test_df, "\n")

# Step 6: Evaluate model on test dataset
errors = 0


for _, row in test_df.iterrows():
    features = [row.feature1, row.feature2]
    true_label = row.label
    pred = knn(train_data, features, k=3)
    print(f"Point {features} → Predicted: {pred}, Actual: {true_label}")
    if pred != true_label:
        errors += 1

# Step 7: Calculate error rate
total = len(test_df)
error_rate = errors / total
print(f"\nTotal Points: {total}")
print(f"Misclassified: {errors}")
print(f"Error Rate: {error_rate:.2f}")
