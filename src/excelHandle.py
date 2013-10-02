import re
import os
from xlrd import open_workbook,cellname


def accnumList(name_sheet):
	""" This function creates list of files corresponding to different experimental treatment groups,
	containing NCBI Accession Numbers of the OTUs """
	filename = []
	directory = os.listdir(".")
	for x in directory:
		spline = x.strip().split(".")
		if spline[1] == "xls":
			filename.append(x.strip())
	wb = open_workbook(filename[0])
	for s in wb.sheets():
		name_sheet.append(s.name.encode('utf-8'))
	for x in name_sheet:
		matches = re.findall('\w+', x)	
		outfile = open("%s.tab" % '_'.join(matches), 'w')
		wb = open_workbook(filename[0])
		for s in wb.sheets():
			if s.name == x:
				for row_index in range(s.nrows):
					for col_index in range(s.ncols):
						outfile.write(s.cell(row_index,col_index).value+"\n")
		outfile.close()
	return