from P1.Seq1 import Seq
PROJECT_PATH = "../P1/PROJECT/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
print('----| Exercise 10 |----')
s1 = Seq()
for gene in gene_list:
    sequence = Seq1.read_fasta(PROJECT_PATH + gene + '.txt')
    print('Gene', gene, ':', 'Most frequent Base:', Seq1.seq_max(sequence))