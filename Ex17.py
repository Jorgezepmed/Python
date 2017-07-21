#MORE FILES

from sys import argv
from os.path import exists              # THIS RETURNS true IF A FILE EXIST

script, from_file, to_file = argv

print "Copying from %s to %s " % (from_file, to_file)

in_file = open(from_file)               #LE DA UN NOMBRE A LA ACCION DE ABRIR EL ARCHIVO EXCISTENTE
indata = in_file.read()                 # GENERA LA ACCION A LEER EL ARCHIV

print "The input data is %d bytes long" % len(indata)   #EL len() NOS LE EL TAMANO DEL ARCHIVO

print "Does the output file exist? %r" % exists(to_file)     #NOS DICE SI EL ARCHIVO A DONDE LO VAMOS A PASAR YA ESTA CREADO O NO
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')              #SE CREA O SE ABRE EL ARCHIVO CON EL NOMBRE ASIGNADO EN argv
out_file.write(indata)                      #ESCIRBE LO QUE LEYO EN EL ARCHIVO ANTEROIR

print "Alright, all done."

out_file.close()
in_file.close()


#CON [ $ echo "texto" > nombre.txt ]  CREAS UN ARCHIVO DE TEXTO
# CON [ $ cat nombre.txt ] ABRES EL ARCHIVO EN CONSOLA
#COMO SE ESCIRBE EN CONSOLA [$ python ex17.py test.txt new_test.txt]
