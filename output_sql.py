import csv, sys

clusters_file = open('cluster_matrix.csv', 'rb')
clusters_reader = csv.reader(clusters_file, delimiter=',')
clusters = []
for rows in clusters_reader:
    clusters.append(rows)

output = open('sql_stuff.sql', 'w')
SSS = "(select nextval('id_seq'), st_multipoint('multipoint (" + "%s 0, " * 29 + "%s 0)', %s)"

def do_write(features, cur, max):
    tu = array_to_tuple(features)
    for i in features:
        output.write(SSS % tu)
        if cur < max-1:
            output.write(",\n")

def write_all(all_the_features):
    output.write("create sequence id_seq start 1;\n")
    output.write("CREATE TABLE sample_mpoints (id integer, geometry st_geometry);\n")
    output.write("INSERT INTO sample_mpoints (id, geometry, label) VALUES\n")
    l = len(all_the_features)
    for i in range(l):
        do_write(all_the_features[i], i, l)

    output.write(";\n")
    output.close()

def array_to_tuple(arr):
    return tuple(arr)

write_all(clusters)
