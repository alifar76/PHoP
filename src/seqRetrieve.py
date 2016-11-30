from itertools import groupby
import os, sys
import subprocess
import re

def fasta_iter(fasta_name):
    """ Given a fasta file. yield tuples of header, sequence """
    fh = open(fasta_name, 'rU')
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        header = header.next()[1:].strip()		# Drop the ">"
        seq = "".join(s.strip() for s in faiter.next())		# Join all sequence lines to one.
        yield header, seq


def fileList(filenames):
	""" This function collects all the files with NCBI Accession IDs corresponding to different
	comparison groups """
	directory = os.listdir(".")
	for x in directory:
		spline = x.strip().split(".")
		if spline[1] == "tab":
			filenames.append(spline[0])
	return filenames

def fastaCreator(name,path):
	""" This function creates FASTA files corresponding to each comparison group """
	acc = []
	infile = open("%s.tab" % name, 'rU')
	for line in infile:
		acc.append(line.strip())
	acc_gg = []
	infile2 = open('%s/gg_13_5_accessions.txt' % path, 'rU')
	for line in infile2:
		if not line.startswith("#"):
			spline = line.strip().split("\t")
			if spline[2] in acc:
				acc_gg.append(spline[0])
				acc.remove(spline[2])
	outfile = open("%s.fna" % name,'w')
	for seq_record in list(fasta_iter("%s/gg_13_5.fasta" % path)):
		if seq_record[0] in acc_gg:
			acc_gg.remove(seq_record[0])
			outfile.write(">"+seq_record[0]+"_"+seq_record[0]+"\n"+str(seq_record[1])+"\n")
	outfile.close()
	return outfile
