# DNA Sequence Analysis
# Beginner bioinformatics project

dna = "ATGCGTACGTTAGC"

# Sequence length
length = len(dna)

# Base counts
a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

# GC content
gc_content = ((g + c) / length) * 100

# DNA to RNA transcription
rna = dna.replace("T", "U")

print("=== DNA SEQUENCE ANALYSIS ===")
print("DNA:", dna)
print("Length:", length)

print("\nBase counts:")
print("A:", a)
print("T:", t)
print("G:", g)
print("C:", c)

print("\nGC content:", round(gc_content, 2), "%")
print("RNA:", rna)
