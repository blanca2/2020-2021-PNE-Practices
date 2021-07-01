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

def info(sequence):
    s = Seq(sequence)
    response = "Total length:" + str(Seq.len(s)) + "\r" + str(Seq.count_bases(s)) + "\r"
    context = {
        'sequence': sequence,
        'information': response,
        'operation': 'info'
    }
    contents = read_template_html_file('./html/operations.html').render(context=context)
    return contents


def comp(sequence):
    s = Seq(sequence)
    complement = s.complement()
    response = complement + '\n'
    context = {
        'sequence': sequence,
        'information': response,
        'operation': 'comp'
    }
    contents = read_template_html_file('./html/operations.html').render(context=context)
    return contents

def rev(sequence):
    s = Seq(sequence)
    rev = s.reverse()
    response = rev + '\n'
    context = {
        'sequence': sequence,
        'information': response,
        'operation': 'Rev'
    }
    contents = read_template_html_file('./html/operations.html').render(context=context)
    return contents

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

def operation(sequence, operation_name):
    if operation_name == "Info":
        result = info(sequence)
    elif operation_name == "Comp":
        result = comp(sequence)
    elif operation_name == "Rev":
        result = rev(sequence)
    context = {
        'sequence': sequence,
        'operation': operation_name,
        'result': result
    }
    contents = read_template_html_file('./html/operations.html').render(context=context)
    return contents



