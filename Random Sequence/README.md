# Random Sequence

###### by Adil Iqbal

### Introduction
The **randomSeq** function is a flexible learning tool for Biopython. It is used to generate a Seq object of any length, using any IUPAC alphabet from the biopython module. This function has utility for those students who either do not yet know how to query data from online databases or who simply do not have access to an internet connection.

### Installatiion
The code can be copy/pasted directly into your code -OR- you can download the python file, store it locally, and import it into your Python project as follows:

```python
from rseq import randomSeq
```

### Usage

Once you have access to the function, use it on your learning adventures! The function returns a Seq object that you can set to any variable. You can then use Biopython to perform all operations on it as usual.

![Common Usage](http://i.imgur.com/Lh118fz.jpg "Common Usage")

### Arguments
The **randomSeq** function takes two arguments, the first one is for the **length of the sequence** that you are requesting and a second one for the **alphabet** that you would like your sequence to use.

#### Supported Alphabets

All IUPAC alphabets are supported. The full list as of April 24th, 2017 is as follows:
- Unambiguous DNA
- Ambiguous DNA
- Extended DNA
- Unambiguous RNA
- Ambiguous RNA
- Protein
- Extended Protein

![IUPAC Alphabet](http://i.imgur.com/Y36aYvE.jpg "IUPAC Alphabet")

#### Optional Arguments

If left undeclared, the **length of the sequence** is chosen randomly between 1 and 100.  If left undeclared, the **alphabet of the sequence** defaults to **Unambiguous DNA**.

![Arguments Optional](http://i.imgur.com/oj0cwNc.jpg "Arguments Optional")

#### Multiple of 3.

The size parameter is always truncated to a multiple of three (3). This feature makes it easier to perform translations operations on your sequences.

![Truncate to 3](http://i.imgur.com/Nr6CfnR.jpg "Truncate to 3")

#### Parameter Validation

Both parameters are validated for an easier debugging experience!

![Validation](http://i.imgur.com/31Bhnax.jpg "Validation")
