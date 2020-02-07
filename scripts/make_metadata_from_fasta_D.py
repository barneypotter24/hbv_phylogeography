from Bio import SeqIO

input_file = "fasta/D/D_with_ancient_aligned.fasta"
output_file_geo = "metadata/D_with_ancient_geo.tsv"
output_file_dates = "metadata/D_with_ancient_dates.tsv"

# Geo
with open(input_file, "r") as handle:
    with open(output_file_geo, 'w') as o:
        o.write("name\tlocation\n")
        for record in SeqIO.parse(handle, "fasta"):
            geo = record.id.split('/')[-2]
            o.write("{}\t{}\n".format(record.id, geo))
        
# Dates
with open(input_file, "r") as handle:
    with open(output_file_dates, 'w') as o:
        o.write("name\tdate\n")
        for record in SeqIO.parse(handle, "fasta"):
            date = record.id.split('/')[-3]
            o.write("{}\t{}\n".format(record.id, date))
            