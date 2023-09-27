#!/usr/bin/env python3

fname = "phylogeography/e/HBV-E_phylogeography.xml"
ofname = "HBV-E_geo.tsv"

with open(ofname, "w") as of:
    of.write("name\tlocation\n")
    with open(fname, "r") as f:
        for line in f.readlines():
            if "taxon id=" in line:
                name = line.split('"')[1]
                of.write(f"{name}\t")
            elif line.startswith("\t\t\t\t") and "<" not in line:
                of.write(line.strip("\t"))
