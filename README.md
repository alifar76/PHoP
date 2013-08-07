PHoP
====

PHoP (PICRUSt Heatmaps of PhyloChip data), pronounced "fop", is a pipeline being developed to visualize PICRUSt results for PhyloChip data. 
The PhyloChip data were obtained from PhyCA algorithm developed by Second Genome. 
The pipeline is written in Python and the heatmaps are created in R. A number of Python and R packages are required prior to running this pipeline:

**Python packages:**

- PICRUSt 0.9.2
- QIIME 1.7.0 (stable public release)
- xlrd 0.9.2
- Biopython 1.61
- Rpy 2.3.6

**R packages:**

- ggplot2 
- reshape2

In addition to these extra packages, the FASTA files (for OTU picking) also need to be dowloaded from Greengenes database:

http://greengenes.secondgenome.com/downloads/database/13_5

Feel free to comment.
