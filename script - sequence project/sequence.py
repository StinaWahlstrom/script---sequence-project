# This file contains a class declaration.
# I have included the initializer and an example method to help you.
# You will need to add the other methods yourself.


class Sequence:

    # This method is the initializer, it is called when creating (instantiating) an object (instance) of this class.
    def __init__(self, bases):
        # store the bases as an attribute.
        self.bases = bases

    # This is an example method, it returns the first base.
    def first_base(self):
        # We can access the 'bases' for this instance via 'self'.
        result = self.bases[0]
        return result

    # TODO: add other methods here to complete the tasks.


    # Task 2
    # Method which counts number of bases in the DNA sequence
    def dna_length(self):
        dna_length = len(self.bases)
        return dna_length

    # Task 3
    # Method that answers if the bases DNA bases?
    def is_dna(self):
        if self.dna_length() == 0:
            return False

        for element in self.bases:
            if element not in ('A', 'T', 'C', 'G'):
                return False

        return True

    # Task 4
    # Method that creates complement string of dna sequence
    def complement_sequence(self):
        new_string = ''
        for element in self.bases:
            if element == 'A':
                new_string = new_string + 'T'
            elif element == 'C':
                new_string = new_string + 'G'
            elif element == 'T':
                new_string = new_string + 'A'
            elif element == 'G':
                new_string = new_string + 'C'
            else:
                return 'error'
        return new_string

    # Task 5
    # Method that finds the first no match bases between two dna sequences
    def first_no_match(self, other):
        for i in range(self.dna_length()):
            if self.bases[i] != other.bases[i]:
                return i
        return -1

    # Task 6
    # Method that
    def read_function(file):
        with open(file, 'r') as sequence:
            lines = sequence.readlines()
            dna = Sequence(str(lines[1]))
            return dna

    # Task 7
    def find_genes(self):
        dna_string = str(self.bases)
        genes_strings = dna_string.split('A{10}T{10}')
        sequence_list = []

        for gene in genes_strings:
            sequence_list.append(Sequence(gene))
        return sequence_list

    # Task 9
    # Finds the number of mutations
    def find_mutations(self, other):
        mutations = 0
        for i in range(self.dna_length()):
            if self.bases[i] != other.bases[i]:
                mutations = mutations + 1
        return mutations













