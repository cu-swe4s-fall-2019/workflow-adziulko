import sys
import gzip
import argparse


def main():
    parser = argparse.ArgumentParser(description=
                                     'takes a gene count file, a gene name, and \
                                     an output file as parameters, and creates a \
                                     file with the sample ids and counts for that gene.')

    parser.add_argument('--gcf', '-gene_count_file',
                        type=str,
                        help='RNA Seq gene file file (gziped)',
                        required=True)

    parser.add_argument('--gn', '-gene_name',
                        type=str,
                        help='Input desired gene name',
                        required=True)

    parser.add_argument('--ofn', '-output_file_name',
                        type=str,
                        help='file with the sample ids and counts for desired gene',
                        required=True)

    args = parser.parse_args()


    gene_count_file = args.gcf
    gene_name = args.gn
    output_file_name = args.ofn


    output_file = open(output_file_name, 'w')

    version = None
    dim = None
    header = None

    count_file = gzip.open(gene_count_file, 'rt')
    for line in count_file:
        striped_line = line.rstrip().split('\t')
        if version is None:
            version = striped_line
            continue
        if dim is None:
            dim = striped_line
            continue
        if header is None:
            header = striped_line
            continue
        if striped_line[1] == gene_name:
            for i in range(2, len(header)):
                output_file.write(header[i] + ' ' + striped_line[i] + '\n')
    count_file.close()
    output_file.close()

if __name__ == '__main__':
    main()
