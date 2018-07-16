#!/usr/bin/python

import sys

f = open(sys.argv[1])

dico = {}

header = f.readline()
seq = f.readline()

while header:
    dico[header.strip()]= seq.strip()
    header = f.readline()
    seq  = f.readline()

f.close()

g = open(sys.argv[2])

line = g.readline()
while line :
    print(line + dico[line])
    line = g.readline()

g.close()
