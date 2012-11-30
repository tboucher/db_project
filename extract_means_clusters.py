from __future__ import division
import csv
import random as rd
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
import time

feature_matrix_file = 'feature_matrix.csv'
k = 40
cluster_output_file = 'cluster_matrix.csv'

features = np.genfromtxt(feature_matrix_file,delimiter=",")

km = MiniBatchKMeans(n_clusters=k, max_iter=300)
km.fit(features[:,2:])

photo_id = 1
cluster_counts = [0]*k
photo_clusters = []

for i in range(len(km.labels_)):
    if photo_id != features[i,1]:
        cluster_counts = [x/sum(cluster_counts) for x in cluster_counts]
        cluster_counts.append(features[i-1,0])
        photo_clusters.append(cluster_counts)
        cluster_counts = [0]*k
        photo_id = features[i,1]

    cluster_counts[km.labels_[i]] += 1

clusters_file = open(cluster_output_file, 'wb')
wr = csv.writer(clusters_file)
for photos in photo_clusters:
    wr.writerow(photos)
clusters_file.close()

# nn-testing..................................
num_neigh = 30

neigh = NearestNeighbors( n_neighbors=num_neigh, algorithm='ball_tree')

cluster_matrix = np.asarray( photo_clusters )
neigh.fit( cluster_matrix[:,0:k] )

gotone = 0
guessedone = 0

for i in range(559):
    [dist, ind] = neigh.kneighbors( cluster_matrix[i,0:k], n_neighbors=num_neigh+1 )
    remainder = i % 5
    img_min = i - remainder
    img_max = img_min + 5
    if any([neighbors in range( img_min, img_max ) for neighbors in ind[0,1:]]):
        gotone += 1

    sample_set = set( xrange( 559 )  ) - set( [i] )
    rand_set = rd.sample( sample_set, num_neigh )
    if any([neighbors in range( img_min, img_max ) for neighbors in rand_set]):
        guessedone += 1

print 'Num. wins: '+str(gotone)
print 'Num. guesses: '+str(guessedone)
print 'N: '+str(num_neigh)
print 'K: '+str(k)
