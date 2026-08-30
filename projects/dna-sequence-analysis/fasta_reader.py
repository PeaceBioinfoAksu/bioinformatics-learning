contains = sequence.replace("T", "U")
# Reverse complement
complement = sequence.translate(str.maketrans("ATGC", "TACG"))
reverse_complement = complement[::-1]
# Display results
print("=== FASTA SEQUENCE ANALYSIS ===")
print("This program analyzes a DNA sequence from a FASTA file.")
print()
print("Header:", header)
print("DNA sequence:", sequence)
print("DNA sequence:", sequence)
print("Sequence length:", len(sequence), "bases")
print("Sequence length:", len(sequence))
# Classify sequence length
if len(sequence) < 20:
    print("Sequence classification: Short sequence")
elif len(sequence) < 100:
    print("Sequence classification: Medium sequence")
else:
    print("Sequence classification: Long sequence")
print("\nBase counts:")
print("A:", a)
print("T:", t)
print("G:", g)
print("C:", c)
print("\nBase frequencies:")
print("A:", round((a / len(sequence)) * 100, 2), "%")
print("T:", round((t / len(sequence)) * 100, 2), "%")
print("G:", round((g / len(sequence)) * 100, 2), "%")
print("C:", round((c / len(sequence)) * 100, 2), "%")
# Check nucleotide diversity
unique_bases = len(set(sequence))

print("\nNucleotide diversity:", unique_bases, "different bases")

if unique_bases == 4:
    print("The sequence contains all four DNA bases.")
else:
    print("The sequence does not contain all four DNA bases.")
print("\nGC content:", round(gc_content, 2), "%")
print("AT content:", round(at_content, 2), "%")
print("GC interpretation:", gc_interpretation)
print("RNA sequence:", rna)
print("Reverse complement:", reverse_complement);arna = sequence.replace("T", "U")
# Reverse complement
complement = sequence.translate(str.maketrans("ATGC", "TACG"))
reverse_complement = complement[::-1]
# Display results
print("=== FASTA SEQUENCE ANALYSIS ===")
print("This program analyzes a DNA sequence from a FASTA file.")
print()
print("Header:", header)
print("DNA sequence:", sequence)
print("Sequence length:", len(sequence))
# Classify sequence length
if len(sequence) < 20:
    print("Sequence classification: Short sequence")
elif len(sequence) < 100:
    print("Sequence classification: Medium sequence")
else:
    print("Sequence classification: Long sequence")
print("\nBase counts:")
print("A:", a)
print("T:", t)
print("G:", g)
print("C:", c)
print("\nBase frequencies:")
print("A:", round((a / len(sequence)) * 100, 2), "%")
print("T:", round((t / len(sequence)) * 100, 2), "%")
print("G:", round((g / len(sequence)) * 100, 2), "%")
print("C:", round((c / len(sequence)) * 100, 2), "%")
# Check nucleotide diversity
unique_bases = len(set(sequence))

print("\nNucleotide diversity:", unique_bases, "different bases")

if unique_bases == 4:
    print("The sequence contains all four DNA bases.")
else:
    print("The sequence does not contain all four DNA bases.")
print("\nGC content:", round(gc_content, 2), "%")
print("AT content:", round(at_content, 2), "%")
print("GC interpretation:", gc_interpretation)
print("RNA sequence:", rna)
print("Reverse complement:", reverse_complement);a
