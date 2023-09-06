def read_strings_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            strings = set(line.strip() for line in file)
        return strings
    except Exception as e:
        print(f'Error reading file {file_path}: {e}')
        return set()

def calculate_precision_recall(file1_path, file2_path):
    set1 = read_strings_from_file(file1_path)
    set2 = read_strings_from_file(file2_path)

    common_strings = set1.intersection(set2)

    precision = len(common_strings) / len(set1) if len(set1) > 0 else 0
    recall = len(common_strings) / len(set2) if len(set2) > 0 else 0

    return precision, recall

# Example usage:
file1_path = 'output/output.6.txt'
file2_path = 'data/benchmarkLEs.csv'

precision, recall = calculate_precision_recall(file1_path, file2_path)
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
