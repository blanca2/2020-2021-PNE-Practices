from Seq1 import test_sequences

def print_result(i, sequence):
    print("Sequence " + str(i) + ": (Lenght: " + str(sequence.len()) + ")" + str(sequence))
    print("Bases:", sequence.count())
    print("Rev:", sequence.reverse())
    print("Comp:", sequence.complement())

print("----- | Practice 1, Exercise 8 | ------")
# We create the test sequences
list_sequences = list(test_sequences())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])