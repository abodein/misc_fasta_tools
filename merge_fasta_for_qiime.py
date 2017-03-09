#!/usr/bin/python2.7

# BUT :
# read files and store in a dico of list which keys are header before _x
# and values are fasta seqs stored in lists
# suppose fasta 1 line

# USAGE:
# merge_fasta_for_qiime.py fichier_1.fa fichier_2.fa > combined_seq.fa

import sys
try:
	fasta1 = sys.argv[1]
	fasta2 = sys.argv[2]
except:
	exit("arg1: fasta1, arg2: fasta2")


def add_to_dico( dico, fichier) :
	""" add to dico """
	tmp = dict(dico)
	f = open(fichier)
	line1 = f.readline() # header
	line2 = f.readline() # seq
	while line1 :
		KEY = line1.split("_")[0]
		VALUE = line2.strip()
		try :
			tmp[ KEY ].append( VALUE )
		except :
			tmp[ KEY ] = [ VALUE ]

		line1 = f.readline() # new header
		line2 = f.readline() # new seq
	f.close()
	return tmp

# read fasta1
dico = {}
dico = add_to_dico( dico, fasta1 )
# read fasta2
dico = add_to_dico( dico, fasta2 )


# write in stdout
for k in dico.keys():
	count = 0
	for s in dico[ k ]:
		print "{0}_{1}".format(k,count)
		print s
		count += 1


