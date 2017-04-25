# Random Sequence
# by Adil Iqbal

from random import randint, randrange
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def randomSeq(size=None, language=IUPAC.unambiguous_dna):
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
        
    # Validate language parameter.
    for i in range(len(valid_langs)):
        if language == valid_langs[i]:
            break
    else:
        print('Language parameter of \'randomSeq\' must be a valid IUPAC alphabet.')
        raise TypeError
        
    # Validate size parameter.
    try:
        size = int(size - (size % 3))
    except:
        print('Size parameter of \'randomSeq\' must be an integer.')
        raise TypeError
        
    # Generate random sequence.
    gene = ""
    for i in range(size):
        roll = randint(0, len(language.letters) - 1)
        gene += language.letters[roll]
        
    return Seq(gene, language)
