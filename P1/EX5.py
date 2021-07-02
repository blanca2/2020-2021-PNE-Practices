from Seq1 import Seq

def print_result(i, sequence):
    print("Sequence" + str(i) + ": (Length: " + str(sequence.len()), ")" + str(sequence))
    a, c, g, t = sequence.count_bases()
    print("A: " +str(a) + ",C :" + str(c) + ",G :"+str(g) + ",T :" + str(t))

print("-----| Practice 1, Exercise 5 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid Sequence")

print_result(1, s1)
print_result(2, s2)
print_result(3, s3)
