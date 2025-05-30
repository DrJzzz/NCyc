import sys

def count_sequences(fasta_file):
    count = 0
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <fasta_file>")
        sys.exit(1)
    fasta_file = sys.argv[1]
    num_sequences = count_sequences(fasta_file)
    print(f"Number of sequences: {num_sequences}")