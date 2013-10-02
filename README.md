#PHoP (PICRUSt Heatmaps of PhyloChip data) v0.1.2

Background
------

PHoP, pronounced "fop", is a pipeline being developed to visualize PICRUSt results for PhyloChip data. The PhyloChip data were obtained from PhyCA algorithm developed by Second Genome. The pipeline is written in Python 2.7.3 and the heatmaps are created in R 2.15.3.

Required Packages
------

**Python:**

- [PICRUSt 1.0.0](http://picrust.github.io/picrust/install.html#install)
- [BIOM 1.2.0](http://biom-format.org/)
- [QIIME 1.7.0 (stable public release)](https://github.com/qiime/qiime-deploy)
- [xlrd 0.6.1](https://pypi.python.org/pypi/xlrd/0.6.1)

**R:**

- [ggplot2](http://ggplot2.org/) 
- [reshape2](http://cran.r-project.org/web/packages/reshape2/index.html)

In addition to these extra packages, two extra files, ```gg_13_5.fasta.gz``` and ```gg_13_5_accessions.txt.gz```, need to be downloaded and extracted from the [Greengenes database](http://greengenes.secondgenome.com/downloads/database/13_5).
For the [OTU Picking via QIIME](http://picrust.github.io/picrust/tutorials/otu_picking.html#otu-picking-tutorial) step, the file ```gg_13_5_otus.tar.gz``` also needs to be downloaded and untarred. 

The pipeline has been tested on Ubuntu 12.04.3 LTS.


How to use
------

All the scripts that are part of the pipeline are present in the src folder. There are 6 scripts in total:

- ```excelHandle.py```
- ```seqRetrieve.py```
- ```qiimeRunner.py```
- ```picrusT.py```
- ```heatMapper.py```
- ```mainScript.py```

To see help with pipeline, simply type the following in the terminal:

```python mainScript.py -h```

This script requires all other scripts to be present in the same working directory.The script also assumes that the input file is also in the working directory. 

The input file should be an Excel file with .xls extension with multiple spreadsheets in it. Each spread sheet should contain a list of NCBI Accession IDs of 16S sequences and should correspond to a specific treatment group. A sample input file is also present within the src/ folder called ```sample.xls```.
