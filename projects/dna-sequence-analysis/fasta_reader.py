# FASTA Sequence Analyzer
# Beginner Bioinformatics Project

filename = "example.fasta"

with open(filename, "r") as file:
    lines = file.readlines()

header = lines[0].strip()
sequence = "".join(line.strip() for line in lines[1:])
# Validate DNA sequence
valid_bases = {"A", "T", "G", "C"}

if not set(sequence).issubset(valid_bases):
    print("Error: FASTA file contains an invalid DNA sequence.")
    exit()
# Base counts
a = sequence.count("A")
t = sequence.count("T")
g = sequence.count("G")
c = sequence.count("C")

# GC content
gc_content = ((g + c) / len(sequence)) * 100
# AT content
at_content = ((a + t) / len(sequence)) * 100
# Interpret GC content
if gc_content < 40:
    gc_interpretation = "Low GC content"
elif gc_content <= 60:
    gc_interpretation = "Moderate GC content"
else:
    gc_interpretation = "High GC content"
# DNA to RNA transcription
rna = sequence.replace("T", "U")
# Reverse complement
complement = sequence.translate(str.maketrans("ATGC", "TACG"))
reverse_complement = complement[::-1]
# Display results
print("=== FASTA SEQUENCE ANALYSIS ===")
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
print("Reverse complement:", reverse_complement);a# Classify sequence length
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
print("RNA sequence:", rna)
print("Reverse complement:", reverse_complement);
