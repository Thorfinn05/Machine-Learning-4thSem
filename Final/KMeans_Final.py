import math
import random
import pandas
import matplotlib.pyplot as plt

def distance(p1, p2):
    total = 0
    for i in range(len(p1)):
        total += (p1[i] - p2[i]) ** 2
    return math.sqrt(total)

def mean(points):
    n = len(points)
    dims = len(points[0])
    result = []
    for i in range(dims):
        s = 0
        for j in range(n):
            s += points[j][i]
        result.append(s/n)
    return result

def kmeans(data, k, max_iters = 100):
    centroids = random.sample(data, k)
    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = []
            for c in centroids:
                d = distance(point, c)
                distances.append(d)
            min_index = distances.index(min(distances))
            clusters[min_index].append(point)
        new_centroids = []
        for cluster in clusters:
            if cluster:
                new_c = mean(cluster)
            else:
                new_c = random.choice(data)
            new_centroids.append(new_c)

        if new_centroids == centroids:
            break
        centroids = new_centroids
    return centroids, clusters
        
df = pd.read_csv('data.csv')
print(df)
data = df.values.tolist()
print(data)

final_centroids, final_clusters = kmeans(data, k=3)

print("Final Centroids: ")
for c in final_centroids:
    f_c = [round(val, 2) for val in c]
    print(f_c)

print("\n Cluster: ")
for i, cluster in enumerate(final_clusters):
    print("Cluster: ", i+1, ":", cluster)

# --- Plotting the Clusters ---
colors = ['red', 'green', 'blue']

for i, cluster in enumerate(final_clusters):
    x_vals = [p[0] for p in cluster]
    y_vals = [p[1] for p in cluster]
    plt.scatter(x_vals, y_vals, color=colors[i], label=f'Cluster {i+1}')

# Plot centroids
cent_x = [c[0] for c in final_centroids]
cent_y = [c[1] for c in final_centroids]

plt.scatter(cent_x, cent_y, color='black', marker='X', s=200, label='Centroids')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering')
plt.legend()
plt.grid(True)
plt.show()