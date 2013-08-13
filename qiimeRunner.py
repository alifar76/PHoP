import os, sys
import subprocess



def paramFile(percent,fraction):
	""" This function creates parameter file for OTU picking through QIIME """
	infile = open("otu_picking_params_%s.txt" % percent, "w")
	infile.write('pick_otus:enable_rev_strand_match True'+'\n')
	infile.close()
	infile2 = open("otu_picking_params_%s.txt" % percent, "a")
	infile2.write('pick_otus:similarity %s' % fraction +'\n')
	infile2.close()
	return infile2

def qiimeRun(filenames):
	""" This function runs QIIME to perform OTU picking """
	directory = os.listdir(".")
	for x in directory:
		spline = x.strip().split(".")
		if spline[1] == "fna":
			filenames.append(spline[0])
	for name in filenames:
		commander = 'pick_closed_reference_otus.py -i $PWD/%s.fna -o $PWD/ucrC97_%s/ -p $PWD/otu_picking_params_97.txt -r $PWD/gg_13_5.fasta' % (name, name)
		subprocess.call([commander],shell=True,)
	return