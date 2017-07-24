#FUNCTIONS AND FILES

from sys import argv

script, input_file = argv

def print_all(f):               #EL ARGUMENTO SE LLAMA f
    print f.read()              #AQUI DECIMOS QUE CUANDO SE LLAME AL ARCHIVO SE SEA

def rewind(f):
    f.seek(2)                   #EL nombre.seek() LE POR PATES O DESINTEGRA


def print_a_line(line_count, f):
    print line_count, f.readline()  #SI HAY UNA COMA AL FINAL DE f,readline() hace que se quite el salto de linea extra
                                    #f.readline  ES PARA UNA ESPECIA DE LEER UNA CORDENADA DE UN ARCHIVO
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)                       #COMO QUE SE DA LA ORDEN DE SEPARAR EL TEXO Y SE DESCOMPONERA EN DIFERNETTES PATRONES 

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
