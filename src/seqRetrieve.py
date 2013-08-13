from Bio import SeqIO
import os, sys
import subprocess
import re


def fileList(filenames):
	""" This function collects all the files with NCBI Accession IDs corresponding to different
	comparison groups """
	directory = os.listdir(".")
	for x in directory:
		spline = x.strip().split(".")
		if spline[1] == "tab":
			filenames.append(spline[0])
	return filenames

def fastaCreator(name):
	""" This function creates FASTA files corresponding to each comparison group """
	acc = []
	infile = open("%s.tab" % name, 'rU')
	for line in infile:
		acc.append(line.strip())
	acc_gg = []
	infile2 = open('gg_13_5_accessions.txt', 'rU')
	for line in infile2:
		if not line.startswith("#"):
			spline = line.strip().split("\t")
			if spline[2] in acc:
				acc_gg.append(spline[0])
				acc.remove(spline[2])
	outfile = open("%s.fna" % name,'w')
	handle = open('gg_13_5.fasta', 'rU')
	records = SeqIO.parse(handle, "fasta")
	for seq_record in records:
		if seq_record.id in acc_gg:
			acc_gg.remove(seq_record.id)
			outfile.write(">"+seq_record.id+"_"+seq_record.id+"\n"+str(seq_record.seq)+"\n")
	outfile.close()
	return outfile