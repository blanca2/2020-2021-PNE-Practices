from P1.Seq1 import Seq
def print_result(i, sequence):
    print("Sequence" + str(i) + ": (Lenght: " + str(sequence.len()) + ") " + str(sequence))
    print("Bases:", sequence.count())
    print("Rev:", sequence.reverse())
    print("Comp:", sequence.complement())

PROJECT_PATH = "../P1/PROJECT/"
print("----- | Practice 1, Exercise 9 | ------")
s1 = Seq()
s1.read_fasta(PROJECT_PATH + "U5.txt")
print_result("", s1)