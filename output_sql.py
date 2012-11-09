import csv

clusters_file = open('cluster_matrix.csv', 'rb')
clusters_reader = csv.reader(clusters_file, delimiter='\t')
clusters = []
for rows in clusters_reader:
    clusters.append(rows)

output = open('sql_stuff.sql', 'w')
SSS = "(select nextval('id_seq'), st_multipoint('multipoint (" + "%s 0," * 29 + "%s 0)', %s),"

def do_write(features):
    tu = array_to_tuple(features)
    for i in features:
        output.write(SSS % tu)

def write_all(all_the_features):
    output.write("create sequence id_seq start 1;")
    output.write("CREATE TABLE sample_mpoints (id integer, geometry st_geometry);\n")
    output.write("INSERT INTO sample_mpoints (id, geometry, label) VALUES\n")
    for i in range(len(all_the_features)):
        do_write(all_the_features[i])
    output.write(";")

def array_to_tuple(arr):
    return tuple(arr)

write_all(clusters)
