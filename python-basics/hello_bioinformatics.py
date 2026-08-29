# DNA sequence analysis

dna = "ATGCGTACGTTAGC"

print("DNA sequence:", dna)
print("Sequence length:", len(dna))

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

print("A:", a)
print("T:", t)
print("G:", g)
print("C:", c)

gc_content = ((g + c) / len(dna)) * 100

print("GC content:", gc_content, "%")
