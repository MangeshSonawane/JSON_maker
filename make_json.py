## make_json.py This is a script to put the lumis from a dataset into a json file.
## Step 1 : Get lumis from DAS
##      dasgoclient --query "run,lumi dataset=<Dataset Name> > lumis.txt"
## Step 2 : Run this script
##      python make_json.py lumis.txt
##
##Author : Mangesh Sonawane
##Email : mangesh.sonawane@cern.ch

import json
import sys

def split_list(numbers):
    sublists = []
    sublist = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1]+1:
            sublist.append(numbers[i])
        else:
            sublists.append(sublist)
            sublist = [numbers[i]]
    sublists.append(sublist)
    return sublists

infile = open(sys.argv[1])
lines = infile.readlines()
for line in lines :
    line = line.split()
    run = line[0]
    lumis = json.loads(line[1])
    lumis.sort()
    sublists = split_list(lumis)
    lumis = []
    for el in sublists :
        lumis.append([el[0],el[-1]])
    print('\"{RUN}\": {LUMIS},').format(RUN=run, LUMIS=lumis)
