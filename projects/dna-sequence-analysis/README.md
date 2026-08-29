# DNA Sequence Analyzer
# Beginner Bioinformatics Project

dna = input("Enter a DNA sequence: ").upper()

# Check if the sequence contains only valid DNA bases
valid_bases = {"A", "T", "G", "C"}

if not dna:
    print("Error: Please enter a DNA sequence.")

elif not set(dna).issubset(valid_bases):
    print("Error: Invalid DNA sequence.")
    print("Only A, T, G, and C are allowed.")

else:
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

    # Display results
    print("\n=== DNA SEQUENCE ANALYSIS ===")
    print("DNA sequence:", dna)
    print("Sequence length:", length)

    print("\nBase counts:")
    print("A:", a)
    print("T:", t)
    print("G:", g)
    print("C:", c)

    print("\nGC content:", round(gc_content, 2), "%")
    print("RNA sequence:", rna)
