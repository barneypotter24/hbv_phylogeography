'''count_sequence_distribution.py

Author: Barney Potter

This defines a script that reads fasta files, categorizing each sequence by country,
    continent, and geographic region as used in the HBV analyses.


'''
import sys
import argparse
from Bio import SeqIO

def fix_country(country):
    country = " ".join(map(lambda x: x.capitalize(), country.lower().split(' '))) #python
    if country == 'Congo':
        country = 'Democratic Republic Of The Congo'
    if country == 'Uk':
        country = 'United Kingdom'
    if country == 'Newzealand':
        country = 'New Zealand'
    if country == 'Newcaledonia':
        country = 'New Caledonia'
    if country == 'Papuanewguinea':
        country = 'Papua New Guinea'
    if country == 'Syrian Arab Republic':
        country = 'Syria'
    if country == 'Republic Of Serbia':
        country = 'Serbia'
    if country == 'Usa' or country == 'United States Of America':
        country = 'United States'
    if country == 'Russian Federation':
        country = 'Russia'
    if country == 'Southafrica':
        country = 'South Africa'
    return country

def parse_country_continent_map():
    '''Turns city_country_full.csv into a dictionary
    '''
    country_continent_file = "metadata/city_country_full.csv"
    with open(country_continent_file,'r') as handle:
        handle.readline()
        d = {}
        for line in handle.readlines():
            line = line.split(',')
            country = fix_country(line[2])
            continent = line[0]
            d[country] = continent
    return d


def parse_country_region_map():
    '''Turns country_region_partial.tsv into a dictionary
    '''
    country_region_file = "metadata/country_region_partial.tsv"
    with open(country_region_file,'r') as handle:
        handle.readline() # skip the header
        d = {}
        for line in handle.readlines():
            line = line.strip().split('\t')
            country = fix_country(line[0])
            region = line[1]
            d[country] = region
    return d

def main(subtype):
    folder = f"fasta/{subtype}/"

    aln_filename = f"{subtype}_with_ancient_aligned.fasta" if subtype !='E' else f"{subtype}_aligned.fasta"

    country_filename = f"metadata/{subtype}_country_sequence_distribution.tsv"
    continent_filename = f"metadata/{subtype}_continent_sequence_distribution.tsv"
    region_filename = f"metadata/{subtype}_region_sequence_distribution.tsv"
    tsv_header = "location\tcount\n"

    country_continent_map = parse_country_continent_map()
    country_region_map = parse_country_region_map()

    country_dict = {}
    continent_dict = {}
    region_dict = {}

    with open(f"{folder}/{aln_filename}", "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            country = fix_country(record.id.split('/')[2])
            # modify country dict
            if country in country_dict.keys():
                country_dict[country] += 1
            else:
                country_dict[country] = 1
            # modify continent dict
            if country_continent_map[country] in continent_dict.keys():
                continent_dict[country_continent_map[country]] += 1
            else:
                continent_dict[country_continent_map[country]] = 1
            # modify region dict
            if country_region_map[country] in region_dict.keys():
                region_dict[country_region_map[country]] += 1
            else:
                region_dict[country_region_map[country]] = 1

    with open(country_filename,'w') as f:
        f.write(tsv_header)
        for key,value in country_dict.items():
            line = f"{key}\t{value}\n"
            f.write(line)

    with open(continent_filename,'w') as f:
        f.write(tsv_header)
        for key,value in continent_dict.items():
            line = f"{key}\t{value}\n"
            f.write(line)

    with open(region_filename,'w') as f:
        f.write(tsv_header)
        for key,value in region_dict.items():
            line = f"{key}\t{value}\n"
            f.write(line)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--subtype')

    args = parser.parse_args()
    assert args.subtype in ['A','D','E'], f"HBV-{args.subtype} was not used in this analysis."


    main(args.subtype)
