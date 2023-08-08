import random


def generate_random_genome(num_chromosomes):
    genome = {}
    nucleotides = ['A', 'T', 'C', 'G']
    max_nucleotides_per_line = 100

    for i in range(1, num_chromosomes + 1):
        num_nucleotides = int(input(f"Enter number of nucleotides for chromosome {i}: "))
        chromosome_sequence = ''.join([random.choice(nucleotides) for _ in range(num_nucleotides)])

        # Split the sequence into lines of 100 nucleotides each
        lines = [chromosome_sequence[j:j + max_nucleotides_per_line] for j in
                 range(0, len(chromosome_sequence), max_nucleotides_per_line)]
        genome[f"Chromosome_{i}"] = lines

    return genome


def export_genome_to_fasta(genome):
    with open('random_genome.fasta', 'w') as fasta_file:
        for chromosome, sequences in genome.items():
            fasta_file.write(f'>{chromosome}\n')
            for sequence in sequences:
                fasta_file.write(f'{sequence}\n')


num_chromosomes = int(input("Enter number of chromosomes: "))
genome = generate_random_genome(num_chromosomes)
export_genome_to_fasta(genome)

print("Random genome has been generated and exported as 'random_genome.fasta'")
