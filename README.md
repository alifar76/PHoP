#PHoP (PICRUSt Heatmaps of PhyloChip data)

Background
------

PHoP, pronounced "fop", is a pipeline being developed to visualize PICRUSt results for PhyloChip data. The PhyloChip data were obtained from PhyCA algorithm developed by Second Genome. The pipeline is written in Python 2.7.3 and the heatmaps are created in R 2.15.3.

Required Packages
------

**Python:**

- [PICRUSt 0.9.2](http://picrust.github.io/picrust/install.html#install)
- [QIIME 1.7.0 (stable public release)](https://github.com/qiime/qiime-deploy)
- [xlrd 0.9.2](https://pypi.python.org/pypi/xlrd/0.9.2)
- [Biopython 1.62](http://biopython.org/wiki/Download)
- [RPy 2.3.6](https://pypi.python.org/pypi/rpy2/)

**R:**

- [ggplot2](http://ggplot2.org/) 
- [reshape2](http://cran.r-project.org/web/packages/reshape2/index.html)

In addition to these extra packages, the two extra files,  ```gg_13_5.fasta.gz``` and ```gg_13_5_accessions.txt.gz```,need to be downloaded and extracted from the [Greengenes database](http://greengenes.secondgenome.com/downloads/database/13_5).


Feel free to comment.
