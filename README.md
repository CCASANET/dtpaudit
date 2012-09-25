# DTP Audit Code

You can use this code to generate audit forms for any patient.

## Instructions

Download this code (or clone via GitHub). In the top level directory create a directory called `dtpfiles`. Then save the following csv files in it: `basic.csv`, `follow.csv`, `visit.csv`, `art.csv`, `lab_cd4.csv`, and `lab_rna.csv`. You can save them as any other name but then you will need to modify the `makeaudit.py` script accordingly. The variables that these files recognized are listed in the beginning of the `cndtp.py` file.

To specify the patients for whom you want to create forms, make a csv file with two columns and no headers. In the first column put the `site` and in the second column place the `patient` ids. Save that file as `ids-for-audit.csv` in the same `dtpfiles` directory.

In the command line, go to the top level directory and type `python makeaudit.py`.

Tada! Your audit files will be in the `auditforms` directory.
