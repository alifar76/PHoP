import os, sys
import subprocess
import itertools
import rpy2.robjects as robjects


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
	r_script = '''
	library(ggplot2); library(reshape2)
	dat <- read.table('New_Plot.txt',sep="\t", quote = "")
	names(dat) <- c("Function", "variable","value")
	diets <- c("Present"="red", "Absent"="grey")
	p1 = ggplot(dat, aes(Function,variable)) + geom_tile(aes(fill = value),
   	colour = "white") + scale_fill_manual(values=diets,name="Biological Function") + theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5,size=20)) + ylab("Category") + xlab("Biological Function")
	ggsave(p1, file = "plot.pdf",width = 40, height = 10)
	diets <- c("Present"="red", "Absent"="grey")
	fileNamer <- function(x){
		u <- read.table(x,sep="\t", quote = "")
		names(u) <- c("Function", "variable","value")
		return(u)
	}
	filenames <- list.files(pattern = "Case")
	for (i in filenames){
		if (file.info(i)$size < 1){
			filenames <- filenames[-which(filenames==i)]
		}
	}
	filelist = list()
	for (i in 1:length(filenames)){
 	filelist[[i]] = fileNamer(filenames[i])
	} 
	for (i in 1:length(filelist)){
		p1 = ggplot(filelist[[i]], aes(Function,variable)) + geom_tile(aes(fill = value),
   		colour = "white") + scale_fill_manual(values=diets,name="Biological Function") + theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5,size=20)) + ylab("Category") + xlab("Biological Function")
		level_label <- paste(levels(filelist[[i]]$variable),collapse='')
		ggsave(p1, file = paste(level_label,".pdf",sep = ""), width = 40, height = 10) 
		}'''
	return robjects.r(r_script)
