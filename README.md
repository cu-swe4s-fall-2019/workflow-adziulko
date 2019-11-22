# Assignment 10: Workflow
Objectives : Express a workflow in a workflow management language.

## Getting Started

- A de-identified, open access version of the sample annotations available in dbGaP. We use this file to extract the brain tissue types of individuals. (11M)
```
$ wget https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
```

- Gene counts.
```
$ wget https://storage.googleapis.com/gtex_analysis_v8/rna_seq_data/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
```

## File Instruction

To get counts for desired gene:
```
$ python get_gene_counts.py --gcf GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --gn SDHB --ofn SDHB_counts.txt
```
--gcf = Input RNA Seq gene file (gziped)

--gn = Input desired gene name

--ofn = Output file with the sample ids and counts for desired gene


To get sample ids for desired tissue type:
```
python get_tissue_samples.py --saf GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --tg Brain --ofn Brain_samples.txt
```

--saf = Input file containing tissue groups and sample IDs

--tg = Desired tissue group

--ofn = Output file with the sample ids for desired tissue group


To make boxplot:
```
python box.py --tgs Brain --gns SDHB --ofn Brain_SDHB.png
```

--tgs = Input tissue id txt file

--gns = Input gene counts txt file 

--ofn = Output file boxplot
