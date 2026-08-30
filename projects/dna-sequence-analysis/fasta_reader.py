# ==========================================
# FASTA SEQUENCE ANALYZER
# Beginner Bioinformatics Project
# ==========================================

# Read FASTA file
with open("example.fasta", "r") as file:
    lines = file.readlines()

# Get header and DNA sequence
header = lines[0].strip()
sequence = "".join(line.strip() for line in lines[1:])
if not header.startswith(">"):
    print("Warning: FASTA header does not start with '>'.")
if not sequence:
    print("Error: No DNA sequence found in the FASTA file.")
    exit()
# Count DNA bases
a = sequence.count("A")
t = sequence.count("T")
g = sequence.count("G")
c = sequence.count("C")

# Calculate GC and AT content
gc_content = ((g + c) / len(sequence)) * 100
at_content = ((a + t) / len(sequence)) * 100

# Interpret GC content
if gc_content < 40:
    gc_interpretation = "Low GC content"
elif gc_content <= 60:
    gc_interpretation = "Moderate GC content"
else:
    gc_interpretation = "High GC content"

# Convert DNA to RNA
rna = sequence.replace("T", "U")

# Reverse complement
complement = sequence.translate(str.maketrans("ATGC", "TACG"))
reverse_complement = complement[::-1]

# Display results
print("=== FASTA SEQUENCE ANALYSIS ===")
print("This program analyzes a DNA sequence from a FASTA file.")
print()

print("Header:", header)
print("DNA sequence:", sequence)
print("Sequence length:", len(sequence), "bases")

# Validate DNA sequence
valid_bases = set("ATGC")
invalid_bases = set(sequence) - valid_bases

if invalid_bases:
    print(
        "Warning: Invalid DNA bases found:",
        ", ".join(sorted(invalid_bases))
    )
else:
    print("DNA sequence validation: Valid")

# Classify sequence length
if len(sequence) < 20:
    print("Sequence classification: Short sequence")
elif len(sequence) < 100:
    print("Sequence classification: Medium sequence")
else:
    print("Sequence classification: Long sequence")

# Display base counts
print("\nBase counts:")
print("A:", a)
print("T:", t)
print("G:", g)
print("C:", c)

# Display base frequencies
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

# Display GC and AT content
print("\nGC content:", round(gc_content, 2), "%")
print("AT content:", round(at_content, 2), "%")
if round(gc_content + at_content, 2) == 100:
    print("GC + AT check: 100%")
else:
    print("Warning: GC + AT content does not equal 100%")
print("GC interpretation:", gc_interpretation)

# Display RNA and reverse complement
print("RNA sequence:", rna)
print("Reverse complement:", reverse_complement)
