#!/usr/bin/env python3

# command line args

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--keys', nargs= '+', required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import numpy as np

# load each of the input paths
total_dict = {}
vector = np.arange(366)

for key in args.keys:
    total_dict[key] = []
    for path in args.input_paths:
        with open(path) as f:
            temp = json.load(f)
            if temp.get(key):
                total_dict[key].append(sum(temp.get(key, 0).values()))
            else:
                total_dict[key].append(0)
    plt.plot(vector, total_dict[key], label = key)
plt.xlabel("Days")
plt.ylabel("Count")
plt.title("Number of Tweets using a certain Hashtag per day")
plt.legend()
plt.show()
plt.savefig("alt_reduce.png", dpi=300)
