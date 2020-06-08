'''make_country_map.py
'''
import sys, os

def main():
    input_file = "metadata/city_country_full.csv"
    output_file = "metadata/country_region_partial.tsv"

    countries_seen = set()

    with open(input_file,'r') as i:
        with open(output_file, 'w') as o:
            header = i.readline()
            o.write("country\tcontinent\n")
            for line in i.readlines():
                line = line.split(',')
                continent = line[0].lower().capitalize()
                country = line[2].lower().capitalize()
                if country not in countries_seen:
                    newline = f"{country}\t{continent}\n"
                    countries_seen.add(country)
                    o.write(newline)

if __name__ == '__main__':
    main()
