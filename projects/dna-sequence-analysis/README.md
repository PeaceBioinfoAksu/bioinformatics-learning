🧬 FASTA Sequence Analyzer

Overview

This project is a beginner bioinformatics tool written in Python.

The program reads a DNA sequence from a FASTA file and performs several basic sequence analyses.

Features

The program can:

- Read a DNA sequence from a FASTA file
- Extract the FASTA header
- Validate the DNA sequence
- Calculate sequence length
- Count A, T, G, and C bases
- Calculate base frequencies
- Calculate GC content
- Calculate AT content
- Transcribe DNA into RNA
- Calculate the reverse complement
- Check nucleotide diversity
- Classify the sequence based on length
- Handle DNA sequences split across multiple FASTA lines

Example Input

>example_dna_sequence
ATGCGTACGTTAGC

Example Output

=== FASTA SEQUENCE ANALYSIS ===
Header: >example_dna_sequence
DNA sequence: ATGCGTACGTTAGC
Sequence length: 14

Base counts:
A: 3
T: 4
G: 4
C: 3

GC content: 50.0 %
AT content: 50.0 %
RNA sequence: AUGCGUACGUUAGC
Reverse complement: GCTAACGTACGCAT

Base frequencies:
A: 21.43 %
T: 28.57 %
G: 28.57 %
C: 21.43 %

Nucleotide diversity: 4 different bases
The sequence contains all four DNA bases.

Sequence classification: Short sequence

Files

- "fasta_reader.py" — Main FASTA analysis program
- "example.fasta" — Example DNA sequence
- "dna_analysis.py" — Earlier version of the DNA analysis program

Skills Practiced

- Python file handling
- FASTA format
- String manipulation
- Sets
- Conditional statements
- Sequence analysis
- Base composition
- GC and AT content
- DNA → RNA transcription
- Reverse complements
- Input validation

Future Improvements

- Support multiple FASTA sequences
- Analyze FASTA files containing many records
- Add codon analysis
- Calculate nucleotide statistics for multiple sequences
- Add command-line arguments
- Improve error handling
- Add automated tests

---

Part of my journey learning Python and bioinformatics. 🧬🐍
