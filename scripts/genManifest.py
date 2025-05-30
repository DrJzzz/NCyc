import os
import sys

def count_fasta_sequences(filepath):
    count = 0
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('>'):
                count += 1
    return count

def main(directory):
    output_file = os.path.join(directory, 'manifest.tsv')
    with open(output_file, 'w') as out:
        out.write("filename\tsequence_count\n")
        for fname in os.listdir(directory):
            if fname.endswith('.fa') or fname.endswith('.fasta'):
                filepath = os.path.join(directory, fname)
                base = os.path.splitext(fname)[0]
                seq_count = count_fasta_sequences(filepath)
                out.write(f"{base}\t{seq_count}\n")
    print(f"Manifest written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory>")
        sys.exit(1)
    main(sys.argv[1])