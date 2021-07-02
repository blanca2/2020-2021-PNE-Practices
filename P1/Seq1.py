from pathlib import Path
import termcolor

def is_valid_sequence(strbases):
    for c in strbases:
        if c != "A" and c != "C" and c != "G" and c != "T":
            return False
    return True

class Seq:
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, strbases=NULL_SEQUENCE):
        self.strbases = strbases
        if strbases == Seq.NULL_SEQUENCE:
            print("NULL seq created")
            self.strbases=strbases
        else:
            if is_valid_sequence(strbases):
                print("New sequence created")
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INCORRECT Sequence detected")



    @staticmethod
    def is_valid_sequence_2(bases):
        for c in bases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    @staticmethod
    def print_seqs(generate_seqs):
        for i in range(0, len(generate_seqs)):
            text = "Sequence" + str(i) + ": (Length: " + str(generate_seqs[i].len()), ")" + str(generate_seqs[i])
            termcolor.cprint(text, 'yellow')

    def __str__(self):
        """Method called when the object is being printed"""
        # --We just return the string with the sequence
        return self.strbases

    def len(self):
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)


    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, g, t
        else:
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                elif ch == "T":
                    t += 1
        return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        dict_bases = {"A": a, "C": c, "G": g, "T": t}
        return dict_bases

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            complement = " "
            for i in self.strbases:
                if i == "C":
                    complement += "G"
                elif i == "G":
                    complement += "C"
                elif i == "A":
                    complement += "T"
                elif i == "T":
                    complement += "A"
            return complement

    def frequent_base(self):
        dict_gene = {"A": 0, "T": 0, "C": 0, "G": 0}
        for d in self.strbases:
            dict_gene[d] +=1
        key_list = list(dict_gene.keys())
        counter = list(dict_gene.values())
        most_frequent = max(counter)
        position = counter.index(most_frequent)
        return key_list[position]

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())


def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid Sequence")
    return s1, s2, s3
