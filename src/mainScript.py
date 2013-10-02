"""
PHoP v0.1.0: PICRUSt Heatmaps of PhyloChip data
Copyright 2013 Ali A. Faruqi

This module produces heatmaps of PICRUSt results using NCBI Accession 
numbers obtained from PhyloChip data.

"""

import argparse
import itertools
from datetime import datetime
import commands
import os
import excelHandle
import seqRetrieve
import qiimeRunner
import picrusT
import heatMapper


def folderCreate(foldernames):
	""" This function creates the folders to organize the data files """
	for folder in foldernames:
		os.system("mkdir %s" % folder)
	return


def mainFunction(path,percentage,otu_folder):
	""" This function runs functions in all other scripts to produce the heatmaps """
	excelHandle.accnumList([])
	all_files = seqRetrieve.fileList([])
	for x in all_files:
		seqRetrieve.fastaCreator(x,path)
	qiimeRunner.paramFile(str(percentage),str(float(percentage/100)))
	qiimeRunner.qiimeRun([],str(percentage),otu_folder)
	picrusT.tableCollect([])
	picrusT.picrustRun([])
	picrusT.biomConvert("ls func_*")
	picrusT.biomConvert("ls metagenome_*")
	all_files2 = heatMapper.fileNamer([])
	for input_file in all_files2:
		label = input_file.split("func_level3_")[1].split(".txt")[0]
		heatMapper.functioNate({},label,input_file)
	heatMapper.uniqueArrange("R_Plot_Data.txt","New_Plot.txt")
	count = 0
	for x in list(itertools.combinations(heatMapper.axesNames([]), 2)):		# 2 is the number of comparison sub-groups between each heatmaps produced. Number can be made more than 2 as well.
		count += 1
		heatMapper.uniIndiv("R_Plot_Data.txt","Case%s.txt"%str(count),x[0],x[1])
	heatMapper.heatmapPlot()
	folderCreate(['1_Excel_Parse', '2_Sequence_Retrieve','3_OTU_Picking','4_PICRUST','5_Functional_Classification','6_Heatmaps'])	
	os.system('mv *.tab 2_Sequence_Retrieve/')
	os.system('mv *.xls 1_Excel_Parse/')
	os.system('mv *.fna 3_OTU_Picking/')
	os.system('mv -f ucrC97* 3_OTU_Picking/')
	os.system('mv func_level3_*.txt 5_Functional_Classification/')
	os.system('mv metagenome*.txt 5_Functional_Classification/')
	os.system('mv Case*.txt 5_Functional_Classification/')
	os.system('mv *.pdf 6_Heatmaps/')
	os.system('mv *.biom 4_PICRUST/')
	os.system('mv R_Plot_Data.txt 5_Functional_Classification/')
	os.system('mv New_Plot.txt 5_Functional_Classification/')
	os.system('mv otu_picking_params_97.txt 3_OTU_Picking/')
	os.system('rm *.pyc')
	os.system('mv heatmapScript.R 6_Heatmaps/')
	return

if __name__ == '__main__':
	startTime = datetime.now()
	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
	description='PICRUSt Heatmaps for PhyloChip Data',
	epilog='''
An example to run the pipeline:
python mainScript.py -d /data/Greengenes_Database_May_2013/gg_13_5_otus/rep_set -ggfiles /data/Greengenes_Database_May_2013 -p 97
	''')
	parser.add_argument('-d', metavar='OTU folder', nargs=1, help='Full path to the folder that contains\
						OTU picking files e.g., /gg_13_5_otus/rep_set',required=True)
	parser.add_argument('-p', metavar='Percentage', type=int ,nargs=1, help='Sequence \
							percentage similarity for OTU picking',required=True)
	parser.add_argument('-ggfiles', metavar='GG Files', nargs=1, help='Full path to the folder that contains\
						Greengenes FASTA/Accession number files',required=True)
	args = parser.parse_args()
	mainFunction(args.ggfiles[0],args.p[0],args.d[0])
	print "\n"+"Task Completed! Completion time: "+ str(datetime.now()-startTime)