from pathlib import Path
def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid sequence")
    return s1, s2, s3
class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"
    def __init__(self, strbases=NULL_SEQUENCE):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == Seq.NULL_SEQUENCE:
            print("NULL sequence created")
            self.strbases = strbases
        else:
            if Seq.is_valid_sequence_2(strbases):
                print("New sequence created")
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INVALID seq!")


    @staticmethod
    def is_valid_sequence_2(bases):
        for c in bases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            print("Sequence", i, ":(Length:", list_sequences[i].len(), ")", list_sequences[i])

    def __str__(self):
        """Method called when the object is being printed"""
        # --We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the lenght of a sequence"""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t= 0, 0, 0, 0
        if not (self.strbases == Seq.NULL_SEQUENCE) and not (self.strbases == Seq.INVALID_SEQUENCE):
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "T":
                    t += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
        return a, c, g, t

    def count(self):
        a, c, t, g = self.count_bases()
        return {'A': a, 'C': c, 'T': t, 'G': g}

    def percentages(self, count_bases, seq_len):
        a = "A:" + str(round(count_bases[0] / seq_len * 100, 2)) + "%"
        c = "C:" + str(round(count_bases[1] / seq_len * 100, 2)) + "%"
        g = "G:" + str(round(count_bases[2] / seq_len * 100, 2)) + "%"
        t = "T:" + str(round(count_bases[3] / seq_len * 100, 2)) + "%"
        return {"A": a, "C": c, "G": g, "T": t}
    @staticmethod
    def frequent_base(dict_count):
        return max(dict_count, key=dict_count.get)

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            complement = ""
            for ch in self.strbases:
                if ch == "A":
                    complement += "T"
                elif ch == "C":
                    complement += "G"
                elif ch == "G":
                    complement += "C"
                elif ch == "T":
                    complement += "A"
        return complement

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())

    def seq_max(self, seq):
        gene_dict = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        for d in seq:
            gene_dict[d] += 1
        self.strbases = max(gene_dict, key=gene_dict.get)
        return self.strbases

