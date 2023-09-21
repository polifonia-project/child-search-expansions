# List of input text files
input_files = [
    "output/60-terms/output.1.txt",
    "output/60-terms/output.2.txt",
    "output/60-terms/output.3.txt",
    "output/60-terms/output.4.txt",
    "output/60-terms/output.5.txt",
    "output/60-terms/output.6.txt",
    "output/60-terms/output.7.txt",
    "output/60-terms/output.8.txt",
    "output/60-terms/output.9.txt",
    "output/60-terms/output.10.txt"]

# Initialize a set to store unique lines
unique_lines = set()

# Iterate through each input file
for file_name in input_files:
    try:
        with open(file_name, "r") as file:
            # Read each line and add it to the set
            for line in file:
                unique_lines.add(line.strip())
    except FileNotFoundError:
        print(f"File not found: {file_name}")

# Output file name
output_file = "output/60-terms/concat_1-10.txt"

# Write the unique lines to the output file
with open(output_file, "w") as output:
    for line in unique_lines:
        output.write(line + "\n")

print(f"Concatenated and removed duplicates from {len(input_files)} files. Result saved in {output_file}")
