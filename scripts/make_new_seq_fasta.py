from Bio import SeqIO

def main():
    a_fasta = "fasta/A/A_with_ancient_unaligned.fasta"
    d_fasta = "fasta/D/D_with_ancient_unaligned.fasta"
    e_fasta = "fasta/E/E_unaligned.fasta"
    a_fasta_o = "fasta/new_sequences/a_new.fasta"
    d_fasta_o = "fasta/new_sequences/d_new.fasta"
    e_fasta_o = "fasta/new_sequences/e_new.fasta"

    new_seq_names = "fasta/new_sequences/new.txt"

    infiles = [a_fasta,d_fasta,e_fasta]
    outfiles = [a_fasta_o,d_fasta_o,e_fasta_o]
    with open(new_seq_names, 'w') as n:
        for i in range(len(infiles)):
            new_records = []
            with open(infiles[i],'r') as ihandle:
                for record in SeqIO.parse(ihandle,"fasta"):
                    if is_new_sequence(record.id):
                        new_records.append(record)
            with open(outfiles[i],'w') as ohandle:
                SeqIO.write(new_records, ohandle, "fasta")
            for record in new_records:
                n.write(f"{record.id}\n")


def is_new_sequence(x):
    if 'MB' in x.split('/')[1]:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
