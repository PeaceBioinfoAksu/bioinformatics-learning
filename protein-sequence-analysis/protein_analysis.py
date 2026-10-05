protein = input("Enter a protein sequence: ").upper()

valid_amino_acids = set("ACDEFGHIKLMNPQRSTVWY")

invalid_amino_acids = set()

for amino_acid in protein:
    if amino_acid not in valid_amino_acids:
        invalid_amino_acids.add(amino_acid)

if invalid_amino_acids:
    print("Error: Invalid amino-acid letters found:", ", ".join(sorted(invalid_amino_acids)))
else:
    print("\n=== PROTEIN SEQUENCE ANALYSIS ===")
    print("Protein sequence:", protein)

    length = len(protein)
    print("Protein length:", length, "amino acids")

    # Amino-acid counts
    print("\nAmino-acid counts:")

    amino_acid_counts = {}

    for amino_acid in protein:
        if amino_acid in amino_acid_counts:
            amino_acid_counts[amino_acid] += 1
        else:
            amino_acid_counts[amino_acid] = 1

    for amino_acid in sorted(amino_acid_counts):
        print(amino_acid + ":", amino_acid_counts[amino_acid])

    # Amino-acid frequencies
    print("\nAmino-acid frequencies:")

    for amino_acid in sorted(amino_acid_counts):
        frequency = (amino_acid_counts[amino_acid] / length) * 100
        print(amino_acid + ":", round(frequency, 2), "%")

    # Most common amino acid
    most_common_amino_acid = max(
        amino_acid_counts,
        key=amino_acid_counts.get
    )

    most_common_count = amino_acid_counts[most_common_amino_acid]

    print("\nMost common amino acid:", most_common_amino_acid)
    print("Most common amino acid count:", most_common_count)

    # Approximate molecular weight
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

    molecular_weight = 0

    for amino_acid in protein:
        molecular_weight += amino_acid_masses[amino_acid]

    print("\nApproximate molecular weight:", round(molecular_weight, 2), "Da")

    # Hydrophobic and hydrophilic analysis
    hydrophobic_amino_acids = set("AVILMFWY")
    hydrophilic_amino_acids = set("RNDQEKHSTCPG")

    hydrophobic_count = 0
    hydrophilic_count = 0

    for amino_acid in protein:
        if amino_acid in hydrophobic_amino_acids:
            hydrophobic_count += 1
        elif amino_acid in hydrophilic_amino_acids:
            hydrophilic_count += 1

    hydrophobic_percentage = (hydrophobic_count / length) * 100
    hydrophilic_percentage = (hydrophilic_count / length) * 100

    print("\nHydrophobic and hydrophilic analysis:")
    print("Hydrophobic amino acids:", hydrophobic_count)
    print("Hydrophilic amino acids:", hydrophilic_count)
    print("Hydrophobic percentage:", round(hydrophobic_percentage, 2), "%")
    print("Hydrophilic percentage:", round(hydrophilic_percentage, 2), "%")

    # Charged amino-acid analysis
    positively_charged = set("KRH")
    negatively_charged = set("DE")

    positive_count = 0
    negative_count = 0

    for amino_acid in protein:
        if amino_acid in positively_charged:
            positive_count += 1
        elif amino_acid in negatively_charged:
            negative_count += 1

    total_charged = positive_count + negative_count
    charged_percentage = (total_charged / length) * 100
    net_charge_tendency = positive_count - negative_count

    print("\nCharged amino-acid analysis:")
    print("Positively charged amino acids:", positive_count)
    print("Negatively charged amino acids:", negative_count)
    print("Total charged amino acids:", total_charged)
    print("Charged amino-acid percentage:", round(charged_percentage, 2), "%")
    print("Net charge tendency:", net_charge_tendency)

    # Amino-acid chemical class analysis
    nonpolar_amino_acids = set("AVILMFWPG")
    polar_amino_acids = set("STNQCY")

    nonpolar_count = 0
    polar_count = 0

    for amino_acid in protein:
        if amino_acid in nonpolar_amino_acids:
            nonpolar_count += 1
        elif amino_acid in polar_amino_acids:
            polar_count += 1

    nonpolar_percentage = (nonpolar_count / length) * 100
    polar_percentage = (polar_count / length) * 100
    positive_percentage = (positive_count / length) * 100
    negative_percentage = (negative_count / length) * 100

    print("\nAmino-acid chemical class analysis:")
    print("Nonpolar amino acids:", nonpolar_count)
    print("Nonpolar percentage:", round(nonpolar_percentage, 2), "%")
    print("Polar amino acids:", polar_count)
    print("Polar percentage:", round(polar_percentage, 2), "%")
    print("Positively charged amino acids:", positive_count)
    print("Positively charged percentage:", round(positive_percentage, 2), "%")
    print("Negatively charged amino acids:", negative_count)
    print("Negatively charged percentage:", round(negative_percentage, 2), "%")

    # Aromatic amino-acid analysis
    aromatic_amino_acids = set("FWY")

    aromatic_count = 0

    for amino_acid in protein:
        if amino_acid in aromatic_amino_acids:
            aromatic_count += 1

    phenylalanine_count = protein.count("F")
    tryptophan_count = protein.count("W")
    tyrosine_count = protein.count("Y")

    aromatic_percentage = (aromatic_count / length) * 100

    print("\nAromatic amino-acid analysis:")
    print("Phenylalanine (F):", phenylalanine_count)
    print("Tryptophan (W):", tryptophan_count)
    print("Tyrosine (Y):", tyrosine_count)
    print("Total aromatic amino acids:", aromatic_count)
    print("Aromatic amino-acid percentage:", round(aromatic_percentage, 2), "%")

    # Protein diversity and complexity
    unique_amino_acids = set(protein)
    unique_count = len(unique_amino_acids)

    diversity_percentage = (unique_count / length) * 100

    print("\nProtein diversity and complexity:")
    print("Unique amino acids:", unique_count)
    print("Unique amino-acid types:", "".join(sorted(unique_amino_acids)))
    print("Sequence diversity percentage:", round(diversity_percentage, 2), "%")

    # Protein sequence validation
    print("\nProtein sequence validation: Valid")
