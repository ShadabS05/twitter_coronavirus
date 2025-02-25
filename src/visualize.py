#!/usr/bin/env python3

# command line args
#
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

keys = [item[0] for item in sorted(items[0:10], key=lambda item: item[1])]
values = [item[1] for item in sorted(items[0:10], key=lambda item: item[1])]
#print(values[0:10])
#print(keys[0:10])

p1 = plt.bar(keys, values, .35)
plt.savefig("country_coronavirus.png", dpi=300, bbox_inches='tight')
plt.show()

#p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)
