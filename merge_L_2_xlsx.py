#!/usr/bin/python

from openpyxl import Workbook
import sys
import re
import os
from argparse import ArgumentParser

def read_params(args):
	parser = ArgumentParser(description = "Merge all _Lx.txt files in a given folder to an uniq .xlsx file")
	parser.add_argument("-i","--input", metavar = "<path_to_input_dir>",required = True, type = str, nargs =1, help = "Path to input folder, where are the Lx.txt files")
	parser.add_argument("-o","--output", metavar = "<path_to_output>", required = True,type = str, nargs = 1, help = "Path to .xlsx output file")
	return parser  


if __name__ == "__main__":
	args = read_params( sys.argv )
	args = vars(args.parse_args())	

	print args
	path = args["input_folder"]
	path_to_out = args["output"]

	# find all table_mc*_Lx.txt
	reg = re.compile("table_.*_L(.)\.txt")
	
	wb = Workbook() # ouverture de l'excel
	wb.remove_sheet(wb.active) # supprime la feuille vide
		
	list_file = sorted([ a for a in os.listdir( path ) if reg.match(a) ])
	
	for fichier in sorted(list_file) :
		num = reg.sub(r'\1',fichier)
		ws = wb.create_sheet()
		ws.title = "L"+num
		
		f = open(path+"/"+fichier)
		line = f.readline() # constructed from biom file
	
		while line :   #add each row to ws
			line = f.readline()
			ws.append(line.split("\t"))
	
	wb.save(path_to_out) 

