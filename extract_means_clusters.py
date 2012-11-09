from __future__ import division
import csv
import numpy as np
from sklearn.cluster import KMeans
import time

start = time.time()
k = 30

features = np.genfromtxt('features.csv',delimiter=",")

km = KMeans(n_clusters=k, max_iter=300)
km.fit(features[:,2:])

photo_id = 1
cluster_counts = [0]*(k+1)
photo_clusters = []
i = 0
for surf_feature in km.labels_:
    if photo_id != features[i,1]:
        cluster_counts = [x/sum(cluster_counts) for x in cluster_counts]
        cluster_counts.append(features[i,0])
        photo_clusters.append(cluster_counts)
        cluster_counts = [0]*k
        photo_id = features[i,1]

    cluster_counts[surf_feature] += 1
    i += 1

clusters_file = open('/home/tommy/Desktop/db_project/clusters.csv', 'wb')
wr = csv.writer(clusters_file)
for photos in photo_clusters:
    wr.writerow(photos)
clusters_file.close()
