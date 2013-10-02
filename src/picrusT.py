import os, sys
import re
import commands
import subprocess


def tableCollect(filenames):
	""" This function collects the OTU tables needed for PICRUSt"""
	working_folder = commands.getstatusoutput('pwd')[1]
	directory = os.listdir(working_folder)
	for x in directory:
		uc_folder = re.compile("ucrC97").search(x)
		if uc_folder:
			fold = os.listdir("%s/%s/" % (working_folder, x)) 
			for y in fold:
				otu_tab = re.compile("otu_table").search(y)
				if otu_tab:
					new_name = x.split("ucrC97_")[1]+".biom"
					os.chdir("%s/%s/" % (working_folder, x))
					os.system("cp  %s %s" % (y, new_name))
					os.system("mv %s ../" % new_name)
	os.chdir("%s/" % working_folder)
	return
	
def picrustRun(filenames):
	""" This function runs PICRUSt """
	directory = os.listdir(".")
	for x in directory:
		biom = re.compile(".biom").search(x)
		if biom:
			filenames.append(x.strip().split(".biom")[0])
	commands_out = ['normalize_by_copy_number.py -i %s.biom -o normalized_%s.biom','predict_metagenomes.py -i normalized_%s.biom -o metagenome_predictions_%s.biom','categorize_by_function.py -i metagenome_predictions_%s.biom -c KEGG_Pathways -l 3 -o func_level3_%s.biom']
	for name in filenames:
		for x in commands_out:
			commander = x % (name,name)
			os.system("%s" % commander)
	return


def biomConvert(val):
	""" This function converts BIOM output files to tab-delimited format """
	p = subprocess.Popen([val], shell=True, stdout=subprocess.PIPE)
	for line in p.stdout:
		converter = 'biom convert -i %s -o %s.txt -b' % (line.strip(),line.strip().split(".")[0])
		os.system("%s" % converter)
	return
