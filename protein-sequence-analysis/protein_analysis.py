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

amino_acid_counts = {}

for amino_acid in sorted(valid_amino_acids):
    count = protein.count(amino_acid)
    if count > 0:
        amino_acid_counts[amino_acid] = count
        print(amino_acid + ":", count)

# Display amino-acid frequencies
print("\nAmino-acid frequencies:")

for amino_acid in sorted(amino_acid_counts):
    count = amino_acid_counts[amino_acid]
    frequency = (count / length) * 100
    print(amino_acid + ":", round(frequency, 2), "%")

# Find the most common amino acid
most_common_amino_acid = max(
    amino_acid_counts,
    key=amino_acid_counts.get
)

most_common_count = amino_acid_counts[most_common_amino_acid]

print("\nMost common amino acid:", most_common_amino_acid)
print("Most common amino acid count:", most_common_count)

# Average amino-acid residue masses in Daltons
amino_acid_masses = {
    "A": 71.08,
    "C": 103.14,
    "D": 115.09,
    "E": 129.12,
    "F": 147.17,
    "G": 57.05,
    "H": 137.14,
    "I": 113.16,
    "K": 128.17,
    "L": 113.16,
    "M": 131.19,
    "N": 114.10,
    "P": 97.12,
    "Q": 128.13,
    "R": 156.19,
    "S": 87.08,
    "T": 101.11,
    "V": 99.13,
    "W": 186.21,
    "Y": 163.17
}

# Calculate approximate molecular weight
molecular_weight = 0

for amino_acid in protein:
    molecular_weight += amino_acid_masses[amino_acid]

print(
    "\nApproximate molecular weight:",
    round(molecular_weight, 2),
    "Da"
)

# Define hydrophobic and hydrophilic amino acids
hydrophobic_amino_acids = set("AVILMFWY")
hydrophilic_amino_acids = set("RNDQEKHSTCPG")

# Count hydrophobic and hydrophilic amino acids
hydrophobic_count = 0
hydrophilic_count = 0

for amino_acid in protein:
    if amino_acid in hydrophobic_amino_acids:
        hydrophobic_count += 1
    elif amino_acid in hydrophilic_amino_acids:
        hydrophilic_count += 1

# Calculate percentages
hydrophobic_percentage = (hydrophobic_count / length) * 100
hydrophilic_percentage = (hydrophilic_count / length) * 100

# Display hydrophobic and hydrophilic analysis
print("\nHydrophobic and hydrophilic analysis:")
print("Hydrophobic amino acids:",
      hydrophobic_count)

print("Hydrophilic amino acids:",
      hydrophilic_count)

print("Hydrophobic percentage:",
      round(hydrophobic_percentage, 2), "%")

print("Hydrophilic percentage:",
      round(hydrophilic_percentage, 2), "%")

print("\nProtein sequence validation: Valid")
