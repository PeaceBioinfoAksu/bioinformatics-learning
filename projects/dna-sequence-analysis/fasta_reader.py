# FASTA Sequence Analyzer
# Beginner Bioinformatics Project

filename = "example.fasta"

with open(filename, "r") as file:
    lines = file.readlines()

header = lines[0].strip()
sequence = "".join(line.strip() for line in lines[1:])

# Base counts
a = sequence.count("A")
t = sequence.count("T")
g = sequence.count("G")
c = sequence.count("C")

# GC content
gc_content = ((g + c) / len(sequence)) * 100

# DNA to RNA transcription
rna = sequence.replace("T", "U")

# Display results
print("=== FASTA SEQUENCE ANALYSIS ===")
print("Header:", header)
print("DNA sequence:", sequence)
print("Sequence length:", len(sequence))

print("\nBase counts:")
print("A:", a)
print("T:", t)
print("G:", g)
print("C:", c)

print("\nGC content:", round(gc_content, 2), "%")
print("RNA sequence:", rna)
