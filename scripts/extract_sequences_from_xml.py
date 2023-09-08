from argh import dispatch_command


def main(fname, alignment=False):
    if not alignment:
        extract_taxa_ids(fname)
    else:
        extract_fasta(fname)


def extract_taxa_ids(fname):
    taxa = set()
    with open(fname, "r") as f:
        for line in f.readlines():
            if "taxon id" in line:
                taxa.add(line.split('\"')[1])
    for t in taxa:
        print(t)


def extract_fasta(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if "<sequence>" in lines[i]:
            seqname = lines[i+1].split('\"')[1]
            print(f">{ seqname }")
            fasta = lines[i+2].strip()
            print(fasta)


if __name__ == '__main__':
    dispatch_command(main)
