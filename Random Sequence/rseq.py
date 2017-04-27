# Random Sequence
# by Adil Iqbal

from random import randint, randrange
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Data import CodonTable

def randomSeq(size=None, lang=IUPAC.unambiguous_dna, table=1, persistent=True, bookend=True):
    is_a_Protein = isProtein(lang)

    if size == None: # If no size was declared, assign it randomly.
        size = randrange(6, 100)

    try: # Validate size parameters.
        size = int(size)
    except:
        print('Size parameter of \'randomSeq\' must be an integer.')

    validateLang(lang) # Validate language parameter.

    if not is_a_Protein:
        size -= size % 3 # Truncate for translation purposes.

    if persistent or bookend:
        codonSets = CodonSets(lang, table)

    # Generate Sequence
    seq = ""
    for i in range(size):
        roll = randint(0, len(lang.letters) - 1)
        seq += lang.letters[roll]
        if len(seq) >= 3 and len(seq) % 3 == 0 and not is_a_Protein :
            # Replace stop codons with non-stop codons.
            if persistent:
                thisCodon = seq[-3:]
                for stopCodon in codonSets.stopCodons:
                    if thisCodon == stopCodon:
                        roll = randint(0, len(codonSets.nonStopCodons) - 1)
                        newCodon = codonSets.nonStopCodons[roll]
                        seq = seq[:-3] + newCodon
                        break
    if bookend: # Put start & stop codons on the respective ends of the sequence.
        roll = randint(0, len(codonSets.startCodons) - 1)
        start = codonSets.startCodons[roll]
        roll = randint(0, len(codonSets.stopCodons) - 1)
        stop = codonSets.stopCodons[roll]
        if is_a_Protein:
            seq = start + seq[1:-1] + stop
        else:
            seq = start + seq[3:-3] + stop

    if persistent or bookend:
        del codonSets

    return Seq(seq, lang)


def isProtein(lang):
    if lang == IUPAC.protein or lang == IUPAC.extended_protein:
        return True
    return False


def validateLang(lang):
    valid_langs = [IUPAC.unambiguous_dna,
                   IUPAC.extended_protein,
                   IUPAC.protein,
                   IUPAC.ambiguous_rna,
                   IUPAC.unambiguous_rna,
                   IUPAC.ambiguous_dna,
                   IUPAC.extended_dna]
    for i in range(len(valid_langs)):
        if lang == valid_langs[i]:
            break
    else:
        print('Language parameter of \'randomSeq\' must be a valid IUPAC alphabet.')
        raise TypeError


class CodonSets:
    def __init__(self, lang, _table):
        self.lang = lang
        self.table = _table
        self.is_a_Protein = isProtein(self.lang)
        self.codonTable = self.getCodonTable()
        self.startCodons = self.codonTable.start_codons
        self.stopCodons = self.codonTable.stop_codons
        self.nonStopCodons = self.getNonStopCodons()
        if self.is_a_Protein:
            self.translateCodons()

    def getCodonTable(self):
        codonTable = None
        if self.lang == IUPAC.unambiguous_dna or self.is_a_Protein:
            codonTable = CodonTable.unambiguous_dna_by_id[self.table]
        elif self.lang == IUPAC.ambiguous_dna:
            codonTable = CodonTable.ambiguous_dna_by_id[self.table]
        elif self.lang == IUPAC.unambiguous_rna:
            codonTable = CodonTable.unambiguous_rna_by_id[self.table]
        elif self.lang == IUPAC.ambiguous_rna:
            codonTable = CodonTable.ambiguous_rna_by_id[self.table]
        return codonTable

    def getNonStopCodons(self):
        if self.lang == IUPAC.unambiguous_rna or self.lang == IUPAC.ambiguous_rna:
            symbols = IUPAC.unambiguous_rna.letters
        else:
            symbols = IUPAC.unambiguous_dna.letters
        nonStopCodons = []
        for nt1 in symbols:
            for nt2 in symbols:
                for nt3 in symbols:
                    codon = nt1 + nt2 + nt3
                    for stopCodon in self.stopCodons:
                        if codon == stopCodon:
                            break
                    else:
                        nonStopCodons.append(codon)
        return nonStopCodons

    def translateCodons(self):
        startAAs = []
        for codon in self.startCodons:
            thisAA = Seq(codon, IUPAC.unambiguous_dna).translate(table=self.table)._data
            startAAs.append(thisAA)
        self.startCodons = startAAs

        stopAAs = []
        for codon in self.stopCodons:
            thisAA = '*'
            stopAAs.append(thisAA)
        self.stopCodons = stopAAs

        nonStopAAs = []
        for codon in self.nonStopCodons:
            thisAA = Seq(codon, IUPAC.unambiguous_dna).translate(table=self.table)._data
            nonStopAAs.append(thisAA)
        self.nonStopCodons = nonStopAAs
