import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description=
                                     'takes a sample attributes files, a tissue \
                                     group ( SMTS ), and output file as parameters, \
                                     and creates a file with all of the samples ids \
                                     ( SAMPID ) for that tissue group.')

    parser.add_argument('--saf', '-sample_attributes_file',
                        type=str,
                        help='File containing tissue groups and sample IDs',
                        required=True)

    parser.add_argument('--tg', '-tissue_group',
                        type=str,
                        help='Desired tissue group (give examples)',
                        required=True)

    parser.add_argument('--ofn', '-output_file_name',
                        type=str,
                        help='file with the sample ids for desired tissue group',
                        required=True)

    args = parser.parse_args()


    sample_attributes_file = args.saf
    tissue_group = args.tg
    output_file_name = args.ofn



    output_file = open(output_file_name, 'w')

    header = None
    sampid_col = -1
    smts_col = -1


    sample_file = open(sample_attributes_file)
    for line in sample_file:
        striped_line = line.rstrip().split('\t')
        if header is None:
            header = striped_line
            sampid_col = striped_line.index('SAMPID')
            smts_col = striped_line.index('SMTS')
            continue

        if striped_line[smts_col] == tissue_group:
            output_file.write(striped_line[sampid_col] + '\n')
    sample_file.close()
    output_file.close()

if __name__ == '__main__':
    main()
