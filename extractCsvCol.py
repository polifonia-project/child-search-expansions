import csv

def extract_column(input_file, output_file, column_index):
    try:
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = [row[column_index] for row in reader]

        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for item in data:
                writer.writerow([item])

        print(f'Successfully extracted and saved column {column_index + 1} to {output_file}.')
    except Exception as e:
        print(f'Error: {e}')

# Example usage:
input_file = 'data/child.csv'
output_file = 'data/benchmarkLEs.csv'
column_index = 1  # Adjust this to select the desired column (0-based index)

extract_column(input_file, output_file, column_index)