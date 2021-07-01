from Seq1 import Seq
import termcolor
import colorama

def print_colored(message, color):
    colorama.init(strip="False")
    print("To server: ", end="")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")
def ping(cs):
    print_colored("PING", "green")
    response = 'OK!'
    cs.send(str(response).encode())

def get(cs, l_seqs, argument):
    print_colored("GET", "yellow")
    response = l_seqs[int(argument)]
    print(response)
    cs.send(response.encode())

def info(cs, argument):
    print_colored("INFO", "yellow")
    sequence = Seq(argument)
    response = "Total length:" + str(sequence.len()) + "\n" + str(sequence.count_bases()) + "\n"
    print(response)
    cs.send(response.encode())

def comp(cs, argument):
    print_colored("COMP", "yellow")
    sequence = Seq(argument)
    response = Seq.complement(sequence) + "\n"
    print(response)
    cs.send(response.encode())

def rev(cs, argument):
    print_colored("REV", "yellow")
    sequence = Seq(argument)
    response = str(sequence.reverse()) + "\n"
    print(response)
    cs.send(response.encode())

def genes(cs, argument):
    print_colored("GENE", "yellow")
    folder = "./SEQS/"
    sequence = Seq()
    print(sequence)
    response = str(sequence.read_fasta(folder + argument + '.txt'))
    print(response)
    cs.send(response.encode())

