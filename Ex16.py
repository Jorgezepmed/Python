#READING AND WRITTING FILES

from sys import argv

script, filename = argv


print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL -C (^C)."
print "if you do want that, hit RETURN."

raw_input("?")                                          #EN REALIDAD ESTE SOLO ES PARA DAR UN ACEPTAR O PAUSA, SIN EL AUN FUNCIONA.

print "Open the file..."
target = open(filename,'a')                             #AQUI ES DONDE SE CREA EL ARCHIVO CON EL NOMBRE DADO CON argv
                                                        #ES ALGUN PARAMETRO RARO EL 'w' 'a'

print "Truncating the file. Gooodbye!"
target.truncate()                                        #EN REALIDAD NO SE PARA QUE FUNCIONA ESTE, SI EL CORRE IGUAL

print "Now i'm going to ask you for three lines. "

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)                                    #SE ESCIRBEN LAS LINEAS EN EL ARCHIVO
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we colse it. "
target.close()                                          #SE GUARDA Y SE CIERRA EL ARCHIVO.


#EN CONSOLA SE ESCRIBE $ python Ex16.py test.txt
