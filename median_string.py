'''
The Motif Finding Problem - Author: Alexandre Lissac
Median String Problem
Works in Python 3.x
example input: ["AAATTGACGCAT", "GACGACCACGTT",
               "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTACGGGACAG"]
output: ACG
References:
	An Introduction to Bioinformatics Algorithms (Jones and Pevzner)
	http://users.cis.fiu.edu/~weiss/cop3337_f99/assignments/turnpike.pdf
'''


class Tree:
    def __init__(self, k, dna_set):
        self.k = k
        self.nucleotides = ['A', 'C', 'G', 'T']
        self.dna_set = dna_set

    def getMedian(self):
        print(self.medianStringProblem(dna_set, self.k))

    def intToDna(self, intergers):
        return ''.join([self.nucleotides[int(elem)-1] for elem in intergers])

    def medianStringProblem(self, dna, l):
        s = [1 for _ in range(l)]
        bestDistance = 1111111111
        bestWord = None
        i = 1
        while i > 0:
            if i < l:
                prefix = ''.join(str(x) for x in s)
                optimisticDistance = self.totalDistance(prefix[0:i], dna)
                if optimisticDistance > bestDistance:
                    s, i = self.bypass(
                        s, i, l, 4)
                else:
                    s, i = self.nextVertex(
                        s, i, l, 4)
            else:
                word = ''.join(str(x) for x in s)
                if self.totalDistance(word, dna) < bestDistance:
                    bestDistance = self.totalDistance(word, dna)
                    bestWord = word
                s, i = self.nextVertex(
                    s, i, l, 4)
        return self.intToDna(bestWord), bestDistance

    def totalDistance(self, pattern, dna):
        total_dist = 0
        for seq in dna:
            widthPattern = len(pattern)
            for i in range(len(seq) - len(pattern) + 1):
                new_pattern_text_dist = self.hamming_distance(
                    pattern, seq[i:i + len(pattern)])
                if (new_pattern_text_dist < widthPattern):
                    widthPattern = new_pattern_text_dist
            total_dist += widthPattern
        return total_dist

    def hamming_distance(self, s1, s2):
        return sum(ch1 != ch2 for ch1, ch2 in zip(self.intToDna(s1), s2))

    def nextVertex(self, a, i, l, k):
        if i < l:
            a[i] = 1
            return a, i+1
        else:
            for j in range(l-1, -1, -1):
                if a[j] < k:
                    a[j] += 1
                    return a, j+1
        return a, 0

    def bypass(self, a, i, l, k):
        for j in range(l, 0, -1):
            if a[j - 1] < k:
                a[j-1] += 1
                return a, j
        return a, 0


if __name__ == "__main__":
    k = 3
    dna_set = ["AAATTGACGCAT", "GACGACCACGTT",
               "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTACGGGACAG"]
    # dna_set = ["ACGT",
    #            "ACGT",
    #            "ACGT"]
    # dna_set = [
    #     "ATA",
    #     "ACA",
    #     "AGA",
    #     "AAT",
    #     "AAC"
    # ]
    # dna_set = [
    #     "AAG",
    #     "AAT",
    # ]
    # dna_set = [
    #     "TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT",
    #     "CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA",
    #     "TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT",
    #     "TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA",
    #     "ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG",
    #     "TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA",
    #     "TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC",
    #     "GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA",
    #     "CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG",
    #     "CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG",
    # ]
    # dna_set = ["TGTTACGTTAAAAGTTTCCTAGATGGAATGTATGGATCTGTA",
    #            "CCATGGGACTGGGTAGATGGCAGTAGAGAAAACCTGCTGAGT",
    #            "GGCGCCATAGATCTGAGGACCCAGCTTGAGGTCTACCAAAGA",
    #            "GTAGATGGAGCCTGCCTAATGCCTTGAGTCAGTTCCAGGAGT",
    #            "GTAGATTGGGTGGATCACATGATAGGACGGATGCAATGCGAC",
    #            "AGAATCCCTCGTACTACCTGTTATGCGTTCATAGATTTTCGA",
    #            "GAGCCTTACTATATTAGGATAGATTCAGGGTTTGCAGTTTAC",
    #            "TACCCAGAGATGCAATCTGTAGATAGCGCTATTATCAGGAGT",
    #            "GTAGATATGACACTGCCATCTCCAGGACTTAGGGGGAAACGT",
    #            "ATAGATGCGGTGCACCTATAACATACTTCTTGGACTAGGAGA"]
    root = Tree(k, dna_set)
    root.getMedian()
