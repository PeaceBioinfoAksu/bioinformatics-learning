# Simple FASTA File Reader
# Beginner Bioinformatics Project

filename = "example.fasta"

with open(filename, "r") as file:
    lines = file.readlines()

header = lines[0].strip()
sequence = "".join(line.strip() for line in lines[1:])

print("=== FASTA FILE ===")
print("Header:", header)
print("Sequence:", sequence)
print("Length:", len(sequence))
