import sequence
import matplotlib.pyplot as plt


# Create an instance of the Sequence class.
example_sequence1 = sequence.Sequence('AGCT')

# Call the first_base method on our instance. Notice that we don't specify the 'self' parameter when we call the method.
example_first_base = example_sequence1.first_base()
print(f'The first base is: {example_first_base}')

# TODO add method calls to complete the tasks

# Task 1

sequence_1 = sequence.Sequence('GTAGTC')
first_base = sequence_1.first_base()
print(f'The first base is: {first_base}')

# Task 2
sequence_length = sequence_1.dna_length()
print(f'The sequence is {sequence_length} bases')

# Task 3
print(f'Sequence 1 is dna: {sequence_1.is_dna()}')
sequence_2 = sequence.Sequence('')
print(f'Sequence 2 is dna: {sequence_2.is_dna()}')
sequence_3 = sequence.Sequence('ATCGH')
print(f'Sequence 3 is dna: {sequence_3.is_dna()}')

# Task 4
print(f'Complement sequence to sequence 1: {sequence_1.complement_sequence()}')

# Task 5
sequence_4 = sequence.Sequence('GTAGCC')
print(f'Index of first no match: {sequence_1.first_no_match(sequence_4)}')

# Task 6
dna = sequence.Sequence.read_function('genome_01.dat')
print(f'genome_01: {dna.bases}')
print(f'Length of genome_01: {dna.dna_length()}')

# Task 7
genes = dna.find_genes()
print(f'Length of first gene: {genes[0].dna_length()}')

# Task 8
gene_lengths = []
for gene in genes:
    gene_lengths.append(gene.dna_length())

plt.hist(gene_lengths)
plt.xlabel('nr of bases')
plt.ylabel('genes')
plt.title('length of genes in genome_01.dat')
plt.savefig('genome_lengths_genome_01')
plt.show()

# Task 9
mutations = []
gene_lengths = []
genes_01 = sequence.Sequence.read_function('genome_01.dat')
genes_02 = sequence.Sequence.read_function('genome_02.dat')
genes_01_genes = genes_01.find_genes()
genes_02_genes = genes_02.find_genes()

for i in range(len(genes_01_genes)):
    mutations.append(genes_01_genes[i].find_mutations(genes_02_genes[i]))
    gene_lengths.append(genes_01_genes[i].dna_length())


print(f'Number of mutations: {mutations}')

plt.scatter(gene_lengths, mutations)
plt.xlabel('dna length')
plt.ylabel('number of mutations')
plt.title('nr of mutations dependence of dna length')
plt.savefig('mutation_dependence_length')
plt.show()

print(f'Total number of mutations {sum(mutations)}')






