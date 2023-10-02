import csv
import json

# Define the input and output file names
input_file = 'data/experiences.csv'
# output_file = 'data/benchmarkLEs.json'
# benchmark_file = 'data/benchmarkLEs.csv'
output_file = 'data/all_lexp.json'
benchmark_file = 'output/30-terms/output.1.txt'

benchmarkData = dict()

# Initialize a set to store LEs
benchmarkLEs = []
with open(benchmark_file, "r") as file:
    # Read each line and add it to the set
    for line in file:
        benchmarkLEs.append(line.strip())

# Open the input CSV file for reading
with open(input_file, 'r', newline='') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)

    # Open the output text file for writing
    with open(output_file, 'w') as txt_file:
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Check if there is at least a 4th column value
            if len(row) >= 4:
                lexp = row[1]
                if (lexp in benchmarkLEs):
                # output all lexps
                # if True:
                    # Replace newline characters with full stops
                    text = row[3].replace('\n', ' ').replace('\r', '').replace('&nbsp;', ' ').strip()
                    benchmarkData[lexp] = text
        txt_file.write(json.dumps(benchmarkData, indent=4))

print(f'Saved JSON to {output_file}.')
# print(json.dumps(benchmarkData, indent=4))

