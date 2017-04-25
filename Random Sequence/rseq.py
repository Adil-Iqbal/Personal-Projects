# Random Sequence
# by Adil Iqbal

from random import randint, randrange
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def randomSeq(size=None, lang=IUPAC.unambiguous_dna):
    valid_langs =  [IUPAC.unambiguous_dna,
                    IUPAC.extended_protein,
                    IUPAC.protein,
                    IUPAC.ambiguous_dna,
                    IUPAC.extended_dna,
                    IUPAC.ambiguous_rna,
                    IUPAC.unambiguous_rna]
                    
    # If no size parameter was declared, generate it randomly.
    if size == None:
        size = randrange(3, 100, 3)
        
    # Validate parameters.
    try:
        size = int(size)
        size -= size % 3
    except:
        print('Size parameter of \'randomSeq\' must be an integer.')
        
    for i in range(len(valid_langs)):
        if lang == valid_langs[i]:
            break
    else:
        print('Language parameter of \'randomSeq\' must be a valid IUPAC alphabet.')
        raise TypeError
        
    # Generate random sequence.
    gene = ""
    for i in range(size):
        roll = randint(0, len(lang.letters) - 1)
        gene += lang.letters[roll]
        
    return Seq(gene, lang)
