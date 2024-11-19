# unsupervised - does not need to be trained
# # builds clusters of data points
# measures dissimilarities
# for interpreting relationship between data points

# Agglomerative Clustering
# type of hierarchical
# treat each data point as a cluster
# groups closest clusters
# repeat until only 1 cluster remains

import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# visualise data points
plt.scatter(x, y)
plt.show()

# compute the ward linkage using euclidean distance, and visualize it using a dendrogram
# for seeing how the cluster is formed?
# turns the data into a set of points
data = list(zip(x, y))
# compute the linkage
linkage_data = linkage(data, method="ward", metric="euclidean")
print(linkage_data)
# show results in a dendrogram
# bottom is indivdual clusters, top is single cluster
dendrogram(linkage_data)
plt.show()

# visualise on a 2d plot, different method than linkage,
# can see the points the clusters are assigned to
hierarchical_cluster = AgglomerativeClustering(
    n_clusters=2, linkage="ward"
)
labels = hierarchical_cluster.fit_predict(data)
plt.scatter(x, y, c=labels)
plt.show()