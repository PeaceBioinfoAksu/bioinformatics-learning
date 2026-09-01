# ==========================================
# PROTEIN SEQUENCE ANALYZER
# Beginner Bioinformatics Project
# ==========================================

# Get protein sequence from the user
protein = input("Enter a protein sequence: ").upper()

# Check if the sequence is empty
if not protein:
    print("Error: Please enter a protein sequence.")
    exit()

# Valid amino-acid letters
valid_amino_acids = set("ACDEFGHIKLMNPQRSTVWY")

# Check protein sequence
invalid_amino_acids = set(protein) - valid_amino_acids

if invalid_amino_acids:
    print(
        "Error: Invalid amino-acid letters found:",
        ", ".join(sorted(invalid_amino_acids))
    )
    exit()

# Calculate protein length
length = len(protein)

# Display results
print("\n=== PROTEIN SEQUENCE ANALYSIS ===")
print("Protein sequence:", protein)
print("Protein length:", length, "amino acids")

# Count amino acids
print("\nAmino-acid counts:")

for amino_acid in sorted(valid_amino_acids):
    count = protein.count(amino_acid)
    if count > 0:
        print(amino_acid + ":", count)

# Display amino-acid frequencies
print("\nAmino-acid frequencies:")

for amino_acid in sorted(valid_amino_acids):
    count = protein.count(amino_acid)
    if count > 0:
        frequency = (count / length) * 100
        print(amino_acid + ":", round(frequency, 2), "%")

print("\nProtein sequence validation: Valid")
