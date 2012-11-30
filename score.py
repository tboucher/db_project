#scoring script

import csv, sys

ID = 0
IL = 1
OL = 2

def readOutput(results_file, limit = 25):
    seen = []
    prev = -1
    with open(results_file, 'rb') as fin:
        reader = csv.reader(fin, delimiter='\t', quoting=csv.QUOTE_NONE)
        line_num = 0
        count = 0
        for row in reader:
            if line_num == 0:
                line_num += 1
                continue
            tokens = row[0].split(';')
            if prev != int(tokens[ID]):
                prev = int(tokens[ID])
                count = 0
            if limit != 0 and count >= limit:
                continue
            if not tokens[ID] in seen and tokens[IL] == tokens[OL]:
                seen.append(tokens[ID])

            count += 1
    print len(seen)

if len(sys.argv) > 2:
    readOutput(sys.argv[1], int(sys.argv[2]))
else:
    readOutput(sys.argv[1])