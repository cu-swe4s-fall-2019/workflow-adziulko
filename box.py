import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse


def main():
    parser = argparse.ArgumentParser(description=
                                     'plot the gene expression distribution across \
                                      a set of genes for a set of tissue groups.')

    parser.add_argument('--tgs', '-tissue_groups',
                        type=str,
                        nargs='+',
                        help='Desired tissue group (give examples)',
                        required=True)

    parser.add_argument('--gns', '-gene_names',
                        type=str,
                        nargs='+',
                        help='Input desired gene name',
                        required=True)

    parser.add_argument('--ofn', '-output_file_name',
                        type=str,
                        help='file with the sample ids for desired tissue group',
                        required=True)

    args = parser.parse_args()


    tissue_groups = args.tgs
    gene_names = args.gns
    output_file_name = args.ofn



    counts = []
    for i in range(len(gene_names)):
        gene = gene_names[i]
    for i in range(len(tissue_groups)):
        tissue = tissue_groups[i]
        #print(tissue)

    sample_to_count_map = {}
    gene_counts_file = open(gene + '_counts.txt')
    for line in gene_counts_file:
        stipped_line = line.rstrip().split()
        sample_to_count_map[stipped_line[0]] = int(stipped_line[1])

    gene_counts_file.close()

    count = []

    tissue_groups_file = open(tissue + '_samples.txt')
    for line in tissue_groups_file:
        sample = line.rstrip()
        if sample in sample_to_count_map:
            count.append(sample_to_count_map[sample])
    tissue_groups_file.close()

    counts.append(count)
    #print(len(tissue_groups))
    #print(len(counts))


    width = len(gene_names) * 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)

    #for i in range(len(tissue_groups)):
    ax = fig.add_subplot(len(gene_names), len(tissue_groups), 1)
    ax.boxplot(count)
    ax.set_xticklabels(gene_names)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title(tissue_groups[i])

    plt.savefig(output_file_name, bbox_inches='tight')

if __name__ == '__main__':
    main()
