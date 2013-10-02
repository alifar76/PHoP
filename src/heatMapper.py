import os, sys
import subprocess
import itertools


def fileNamer(filenames):
	""" This function selects files for heatmap construction """
	val = "ls func_*.txt"
	p = subprocess.Popen([val], shell=True, stdout=subprocess.PIPE)
	for line in p.stdout:
		filenames.append(line.strip())
	return filenames

def funcList(input_file):
	functions = []
	infile = open(input_file,'rU')
	for line in infile:
		if not line.startswith("#"):
			spline = line.strip().split("\t")
			functions.append(spline[0])
	return functions

def functioNate(dictionary,description,filename):
	""" This function creates intermediary data file """
	infile = open(filename, 'rU')
	for line in infile:
		if not line.startswith("#"):
			spline = line.strip().split("\t")
			if  sum([float(i) for i in spline[1:]]) != 0:
				dictionary[spline[0]] = "Present"
			if  sum([float(i) for i in spline[1:]]) == 0:
				dictionary[spline[0]] = "Absent"
	outfile = open("R_Plot_Data.txt",'a')
	for x in funcList(fileNamer([])[0]):					# List of 333 functions predicted by PICRUSt at level 3 of categorization
		outfile.write(x+"\t"+description+"\t"+dictionary[x]+"\n")
	outfile.close()
	return outfile

def uniqueArrange(filename,output):
	""" This function selects discriminatory biological functions between all comparison groups """
	functions = []
	infile = open(filename,'rU')
	for line in infile:
		spline = line.strip().split("\t")
		functions.append(spline[0])
	unique = list(set(functions))
	outfile = open(output, "w")
	for x in unique:
		checker = []
		infile = open(filename,'rU')
		for line in infile:
			spline = line.strip().split("\t")
			if spline[0] == x:
				checker.append(spline[2])
		if len(list(set(checker))) != 1:
			infile = open(filename,'rU')
			for line in infile:
				spline = line.strip().split("\t")
				if spline[0] == x:
					outfile.write(line.strip()+"\n")
	outfile.close()
	return outfile
				
def uniIndiv(filename,output,case1,case2):
	""" This function selects unique biological functions between 2 comparison groups """
	functions = []
	infile = open(filename,'rU')
	for line in infile:
		spline = line.strip().split("\t")
		functions.append(spline[0])
	unique = list(set(functions))
	outfile = open(output, "w")
	for x in unique:
		checker = []
		infile = open(filename,'rU')
		for line in infile:
			spline = line.strip().split("\t")
			if (spline[0] == x and spline[1] == case1):
				checker.append(spline[2])
			if (spline[0] == x and spline[1] == case2):
				checker.append(spline[2])
		if len(list(set(checker))) != 1:
			infile = open(filename,'rU')
			for line in infile:
				spline = line.strip().split("\t")
				if (spline[0] == x and spline[1] == case1):
					outfile.write(line.strip()+"\n")
				if (spline[0] == x and spline[1] == case2):
					outfile.write(line.strip()+"\n")		
	outfile.close()
	return outfile

def axesNames(all_labels):
	infile = open("R_Plot_Data.txt", 'rU')
	for line in infile:
		spline = line.strip().split("\t")
		all_labels.append(spline[1])
	labels = list(set(all_labels))
	return labels


def heatmapPlot():
	""" This function contains the R script used to make the heatmaps """
	outfile = open("heatmapScript.R", "w")
	outfile.write(
	'library(ggplot2); \n\
	dat <- read.table("New_Plot.txt",sep="\t", quote = "") \n\
	names(dat) <- c("Function", "variable","value") \n\
	color_code <- c("Present"="red", "Absent"="grey") \n\
	p1 = ggplot(dat, aes(Function,variable)) + geom_tile(aes(fill = value), \n\
   	colour = "white") + scale_fill_manual(values=color_code,name="Biological Function") + theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5,size=20)) + ylab("Category") + xlab("Biological Function") \n\
	ggsave(p1, file = "plot.pdf",width = 40, height = 10) \n\
	color_code <- c("Present"="red", "Absent"="grey") \n\
	fileNamer <- function(x){ \n\
		u <- read.table(x,sep="\t", quote = "") \n\
		names(u) <- c("Function", "variable","value") \n\
		return(u) \n\
	} \n\
	filenames <- list.files(pattern = "Case") \n\
	for (i in filenames){ \n\
		if (file.info(i)$size < 1){ \n\
			filenames <- filenames[-which(filenames==i)] \n\
		} \n\
	} \n\
	filelist = list() \n\
	for (i in 1:length(filenames)){ \n\
 	filelist[[i]] = fileNamer(filenames[i]) \n\
	} \n\
	for (i in 1:length(filelist)){ \n\
		p1 = ggplot(filelist[[i]], aes(Function,variable)) + geom_tile(aes(fill = value), \n\
   		colour = "white") + scale_fill_manual(values=color_code,name="Biological Function") + theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5,size=20)) + ylab("Category") + xlab("Biological Function") \n\
		level_label <- paste(levels(filelist[[i]]$variable),collapse='') \n\
		ggsave(p1, file = paste(level_label,".pdf",sep = ""), width = 40, height = 10) \n\
		}')
	outfile.close()
	os.system("Rscript heatmapScript.R")
	return
