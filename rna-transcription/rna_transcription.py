transcription = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def to_rna(dna_strand):
    return ''.join(transcription[n] for n in dna_strand)