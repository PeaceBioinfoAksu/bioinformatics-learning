DNA Sequence Analysis

A beginner bioinformatics project written in Python for analyzing DNA sequences.

Project Overview

This project contains two Python programs for working with DNA sequences:

- "dna_analysis.py" — analyzes a DNA sequence entered manually by the user.
- "fasta_reader.py" — reads a DNA sequence from a FASTA file and performs a more detailed analysis.

Features

DNA Sequence Analyzer

The "dna_analysis.py" program:

- Accepts a DNA sequence from the user
- Converts lowercase input to uppercase
- Validates DNA bases
- Calculates sequence length
- Counts A, T, G, and C bases
- Calculates GC content
- Converts DNA to RNA

FASTA Sequence Analyzer

The "fasta_reader.py" program:

- Reads DNA sequences from a FASTA file
- Checks for an empty FASTA file
- Checks for a missing FASTA header
- Converts lowercase DNA to uppercase
- Validates DNA bases
- Detects ambiguous "N" bases
- Counts ambiguous bases
- Classifies sequence length
- Calculates base frequencies
- Calculates GC and AT content
- Checks GC + AT consistency
- Calculates nucleotide diversity
- Converts DNA to RNA
- Calculates the reverse complement

Example FASTA Input

>example_dna_sequence
ATGCGTACGTTAGC

Example Output

Sequence length: 14 bases
DNA sequence validation: Valid
Sequence classification: Short sequence

Base counts:
A: 3
T: 4
G: 4
C: 3

GC content: 50.0 %
AT content: 50.0 %
GC + AT check: 100%
GC interpretation: Moderate GC content

RNA sequence: AUGCGUACGUUAGC
Reverse complement: GCTAACGTACGCAT

Skills Demonstrated

This project demonstrates beginner Python and bioinformatics concepts including:

- Variables
- Strings
- File handling
- Conditional statements
- Loops and string processing
- Sets
- Sequence validation
- Base counting
- Percentage calculations
- DNA → RNA transcription
- Reverse complements
- FASTA file processing

Project Structure

dna-sequence-analysis/
├── dna_analysis.py
├── fasta_reader.py
├── example.fasta
└── README.md

Purpose

This project is part of my bioinformatics learning journey and demonstrates the use of Python to perform basic DNA sequence analysis.
