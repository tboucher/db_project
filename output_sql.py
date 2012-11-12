import csv, sys

clusters_file = open('cluster_matrix.csv', 'rb')
clusters_reader = csv.reader(clusters_file, delimiter=',')
clusters = []
for rows in clusters_reader:
    clusters.append(rows)

output = open('sql_stuff.sql', 'w')
SSS = "(nextval('id_seq'), 'multipoint (" + "%s 0, " * 29 + "%s 0)', %s)"

def do_write(features, cur, max, TO_WRITE_OUT):
    tu = array_to_tuple(features)
    TO_WRITE_OUT += (SSS % tu)
    if cur < max-1:
        TO_WRITE_OUT += ",\n"

    return TO_WRITE_OUT

def write_all(all_the_features):
    TO_WRITE_OUT = ""
    output.write("create sequence id_seq start 1;\n")
    output.write("CREATE TABLE sample_mpoints (id integer, features geometry, label integer);\n")
    output.write("INSERT INTO sample_mpoints (id, features, label) VALUES\n")
    l = len(all_the_features)
    for i in range(l):
        TO_WRITE_OUT = do_write(all_the_features[i], i, l, TO_WRITE_OUT)

    output.write(TO_WRITE_OUT)
    output.write(";\n")
    output.close()

def array_to_tuple(arr):
    return tuple(arr)

write_all(clusters)
