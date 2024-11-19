# another unsupervised method for clustering data points
# iteratively divides data points into K clusters
# minimising variance in each cluster
# K is the number of clusters

# use elbow method to estimate best k val

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

plt.scatter(x, y)
plt.show()

# using the elbow method
data = list(zip(x, y))
inertias = []

# start at one as is the number of clusters
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1, 11), inertias, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# the elbow is the point at which the inertia starts decreasing linearly
# it is a good estimate

# therefore K = 2
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
plt.scatter(x, y, c=kmeans.labels_)
plt.show()
