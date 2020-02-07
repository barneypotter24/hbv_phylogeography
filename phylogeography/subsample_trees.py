import argparse
import sys

parser = argparse.ArgumentParser("Subsample some trees")
parser.add_argument("-i", "--input_file", type=str, help="name of the .trees file to subsample")
parser.add_argument("-o", "--output_file", type=str, help="name of the .trees file that should be output")
parser.add_argument("--subsample_every", type=int, default=None, help="sample every Nth tree from the input")
parser.add_argument("--subsample_total", type=int, default=None, help="sample to a total of N trees")

args = parser.parse_args()

assert bool(args.subsample_every) != bool(args.subsample_total); "Only one method of subsampling should be given."

print("Subsampling input file: {}".format(args.input_file))

if args.subsample_every:
    subsample_every = args.subsample_every
else:
    subsample_every = 0

with open(args.input_file, "r") as i:

    file_lines = len(i.readlines())
    print("file_lines: {}".format(file_lines))

with open(args.input_file, "r") as i:
    this_line = 0
    subcounter = 0
    with open(args.output_file, "w") as o:
        for line in i.readlines():
            this_line += 1
            if "tree STATE" not in line:
                o.write(line)
            else:
                # We already know how often to subsample
                if subsample_every:
                    subcounter += 1
                    if subcounter % subsample_every == 0:
                        o.write(line)
                    else:
                        pass
                # We need to calculate how frequently we need to subsample
                elif args.subsample_total:
                    subcounter += 1
                    total_trees = file_lines-this_line
                    subsample_every = total_trees // args.subsample_total
                    print("total_trees: {}".format(total_trees))
                    print("sampling every: {}".format(subsample_every))
                    # This should probably never happen unless you are subsampling every 1.
                    # Whuch would be silly.
                    if subcounter % subsample_every == 0:
                        o.write(line)
                    else:
                        pass
                else:
                    print("Something is rotten")
                    sys.exit(1)
