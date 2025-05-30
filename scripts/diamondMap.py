import sys
import os

'''
This script processes a DIAMOND output file and maps gene IDs to their corresponding names using a provided mapping file.
Usage:
python diamondMap.py <input.diamond> <input.map>

Where:
- <input.diamond> is the DIAMOND output file.
- <input.map> is the mapping file containing gene IDs and their corresponding names.
'''

def load_map(map_file):
    gene_map = {}
    with open(map_file, 'r') as mf:
        for line in mf:
            parts = line.strip().split()
            if len(parts) >= 2:
                gene_map[parts[0]] = parts[1:]
    return gene_map

def process_diamond(diamond_file, gene_map):
    # Create output file name
    base, ext = os.path.splitext(diamond_file)
    output_file = f"{base}.mapped{ext}"
    with open(diamond_file, 'r') as df, open(output_file, 'w') as out:
        for line in df:
            if line.strip() == "":
                continue
            cols = line.strip().split()
            if len(cols) < 2:
                continue
            gene_id = cols[1]
            mapped_gene = 'NONE'
            if gene_id in gene_map:
                mapped_gene = ' '.join(gene_map[gene_id])
            # Insert mapped_gene as a new column after gene_id (second column)
            new_cols = cols[:2] + [mapped_gene] + cols[2:]
            out.write('\t'.join(new_cols) + '\n')
    print(f"Output written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diamondMap.py <input.diamond> <input.map>")
        sys.exit(1)
    diamond_file = sys.argv[1]
    map_file = sys.argv[2]
    gene_map = load_map(map_file)
    process_diamond(diamond_file, gene_map)