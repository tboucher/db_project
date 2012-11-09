from __future__ import division
import csv
import random as rd
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors

feature_matrix_file = 'feature_matrix.csv'
k = 30
cluster_output_file = 'cluster_matrix.csv'

features = np.genfromtxt(feature_matrix_file,delimiter=",")

km = MiniBatchKMeans(n_clusters=k, max_iter=300)
km.fit(features[:,2:])

photo_id = 1
cluster_counts = [0]*k
photo_clusters = []
i = 0
for surf_feature in km.labels_:
    if photo_id != features[i,1]:
        cluster_counts = [x/sum(cluster_counts) for x in cluster_counts]
        cluster_counts.append(features[i-1,0])
        photo_clusters.append(cluster_counts)
        cluster_counts = [0]*k
        photo_id = features[i,1]

    cluster_counts[surf_feature] += 1
    i += 1

clusters_file = open(cluster_output_file, 'wb')
wr = csv.writer(clusters_file)
for photos in photo_clusters:
    wr.writerow(photos)
clusters_file.close()

# nn-testing..................................
num_neigh = 20

neigh = NearestNeighbors( n_neighbors=num_neigh, algorithm='ball_tree')

cluster_matrix = np.asarray( photo_clusters )
neigh.fit( cluster_matrix[:,0:k] )

trials = 1000
gotone = 0
for i in range(trials):
    randi = rd.randint(0,558)
    [dist, ind] = neigh.kneighbors( cluster_matrix[randi,0:k], n_neighbors=num_neigh )
    remainder = randi % 5
    img_min = randi - remainder
    img_max = img_min + 5
    if any([neighbors in range( img_min, img_max ) for neighbors in ind[0,1:]]):
        gotone += 1

print 'Num. trials: '+str(trials)
print 'Num. wins: '+str(gotone)
print 'N: '+str(num_neigh)
print 'K: '+str(k)

# P(of picking a self photo) = 4/556
# E(of picking a self photo in n-neighbors) = (4/556) * (n-1)

