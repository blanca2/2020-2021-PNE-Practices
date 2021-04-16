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
            if Seq.is_valid_sequence(strbases):
                print("New sequence created")
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INVALID seq!")

    @staticmethod
    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = "Sequence" + str(i) + ":(Length:", str(list_sequences[i].len()) + ")" + str(list_sequences[i])
            termcolor.cprint(text, "yellow")

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
