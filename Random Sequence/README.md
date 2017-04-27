# Random Sequence

###### by Adil Iqbal

### Introduction
The **randomSeq** function is a flexible learning tool for Biopython. It is used to generate a Seq object of any length, using any IUPAC alphabet from the biopython module. This function has utility for those students who either do not yet know how to query databases or who simply do not have access to an internet connection.

### Installation
The code can be copy/pasted directly into your project -OR- you can download the python file, store it locally, and import it into your Python project as follows:

```python
from rseq import randomSeq
```

### Usage

Once you have access to the function, use it on your learning adventures! The function returns a randomly generated Biopython Seq object that you can set to any variable. You can then use Biopython to perform all operations on it as usual.

![Common Usage](http://i.imgur.com/1dRlekE.jpg "Common Usage")

### Arguments
The **randomSeq** function takes several arguments. Below is a sequential list of arguements and their default values. 
1. The *size* parameter defaults to a random integer between 6 and 100 inclusively.
2. The *lang* parameter defaults to unambiguous DNA.
3. The *bookend* parameter defaults to True.
4. The *persistent* paramter defaults to True.
5. The *table* parameter defaults to the Standard NCBI codon table (id=1).

The corresponding subsection below details the behavior of these arguements.

#### Size Parameter
The *size* parameter is an optional parameter that denotes the **length of sequence** that is returned by the function. If the size parameter remains undeclared, a sequence of randomly chosen length (between 6 and 100) will be returned. 

![Using the size parameter](http://i.imgur.com/E4RbfEQ.jpg)
*In the example above, the "my_seq1" object has a constant length of 12 because the size parameter was declared by the user, while the "my_seq2" object has a sequence of random length because the size parameter was not declared.*

The size parameter is **truncated to a multiple of three (3) for all non-protein alphabets.** This is done to ensure that all translation operations proceed without error.

![Size truncation](http://i.imgur.com/p9xw5Yt.jpg "Size truncation")

*In the example above, different sizes are tested to observe behavior. In Group A, the declared size is a multiple of three (3), so its length was expressed in the sequence without truncation. In Group B, the declared sizes were **not** a multiple of three (3), so they were truncated to allow for translation. In Group C, the declared sizes were also **not** a multiple of three (3), but since they are both proteins (therefore, cannot be translated), truncation did not occur.*

#### Supported Alphabets

As you may have guessed, this function can generate sequences based on the alphabet that is declared in the *lang* parameter.  If left undeclared, the alphabet of the sequence defaults to **Unambiguous DNA**. All IUPAC alphabets are supported. The full list as of April 24th, 2017 is as follows:
- Unambiguous DNA
- Ambiguous DNA
- Extended DNA
- Unambiguous RNA
- Ambiguous RNA
- Protein
- Extended Protein

![IUPAC Alphabet](http://i.imgur.com/he2a4pe.jpg "IUPAC Alphabet")
*In the above example, we see just a few demonstrations of the IUPAC alphabets that are supported. Note that the "my_seq1" object generated Unambiguous DNA because the "lang" parameter was not declared.  At the bottom of the example, we can also see that the function was called on the "my_seq" variable without declaring an alphabet. We can see directly that the alphabet attribute is "IUPAC**UnambiguousDNA**()"*

#### Bookend Parameter

The *bookend* parameter is set to True by default.  When the bookend parameter is True, the generated sequence will always begin with start codon (or corresponding amino acid) and always end with a stop codon.  

![Bookend Example](http://i.imgur.com/9DjEhbE.jpg "Bookend Example")
*In the above example, we see that all sequences are generated using unambiguous DNA and then translated to show us the amino acids that are being encoded. In the control group, the "bookend" parameter is set to False. The resulting sequences have neither a start codon or a stop codon. Whereas in the experimental group (that have the "bookend" paramter set to True), we see that each sequence begins with a Leucine (L) or Methionine (M) amino acid, both of which happen to be encoded by a start codon. Each sequence in the experimental group ends in a stop codon, denoted by the astrisks. In this example, codons were defined based on the Standard NCBI Codon Table.*

#### Persistent Parameter

The *persistent* parameter is set to True by default. When the persistent parameter is True, the generated sequence will not contain a stop codon ***within*** the sequence.

![Persistent Example](http://i.imgur.com/mAers4P.jpg "Persistent Example")
*In the above example, we see that all sequences are generated using unambiguous DNA and then translated to show us the amino acids that are being encoded. In the control group, the "persistent" parameter is set to False. The resulting sequences are littered with stop codons (as denoted by asterisks) throughout. In the experimental group, the "persistent" parameter is set to True, and we do not see any stop codons (as denoted by asterisks) **within** the sequences except, of course, for the stop codons at the end of the sequences. In this example, codons were defined based on the Standard NCBI Codon Table.*

#### Table Parameter

By altering the *table* parameter, all codons will be generated based on the codon table of your choosing. The default value is set to 1, which denotes the Standard NCBI Codon Table. 

To learn more about these codon tables, you can visit: **[The Genetic Codes](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi "The Genetic Codes")**

Alternatively, you can take a peek at the Biopython source code repository: **[Codon Table File](https://github.com/biopython/biopython/blob/master/Bio/Data/CodonTable.py "Codon Table File")** (relavent code begins on line 477)

![Table Example](http://i.imgur.com/7cDnPtY.jpg "Table Example")
*In the above example, we see that all sequences are generated using unambiguous DNA and then translated to show us the amino acids that are being encoded. Furthermore, all sequences are generated using Codon Table 6, which is the "Ciliate Nuclear" genetic code. The control group is translated using the exact same table, which yeilds the expected result of sequences that end in a stop codon (denoted by an astrisk) and do not contain any stop codons (denoted by an astrisk) **within** the sequence. The experimental group, however, is translated using Codon Table 5, which is the "Invertebrate Mitochondrial" genetic code. This code was chosen for the demonstration because it does not share any common stop codons with the "Ciliate Nuclear" genetic code. The result is that all sequences in the experiemental group have had their stop codons replaced by an amino acid. Furthermore, stop codons (denoted by an asterisk) have been introduced **within** the experimental sequence despite the "persistent" parameter being set to True.*
