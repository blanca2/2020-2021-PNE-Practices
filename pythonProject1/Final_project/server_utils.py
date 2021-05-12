from Seq1 import Seq
import termcolor
import colorama
import jinja2
import pathlib

def read_template_html_file(filename):
    #create template object, can't be directly sent to the browser as it only reads plain text, files or html (template is none of them), we transform it by render function
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

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

def get(l_seqs, number_seq):
    context = {
        "number": number_seq,
        "sequence": l_seqs[int(number_seq)]
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents

def info(cs, argument):
    print_colored("INFO", "yellow")
    sequence = Seq(argument)
    response = "Total length:" + str(sequence.len()) + "\n" + str(sequence.count_bases()) + "\n"
    print(response)
    cs.send(response.encode())

def comp(cs, argument):
    print_colored("COMP", "yellow")
    sequence = Seq(argument)
    response = str(sequence.complement()) + "\n"
    print(response)
    cs.send(response.encode())

def rev(cs, argument):
    print_colored("REV", "yellow")
    sequence = Seq(argument)
    response = str(sequence.reverse()) + "\n"
    print(response)
    cs.send(response.encode())

def gene(seq_name):
    PATH = "./Sequences/" + seq_name + ".txt"
    s = Seq()
    s.read_fasta(PATH)
    context = {
        "gene_name": seq_name,
        "gene_contents": s.strbases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents


