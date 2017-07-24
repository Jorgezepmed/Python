#PARAMETERS, UNPACKING, VARIABLES

from sys import argv                      #EL [import] ES COMO LLAMAR UNA LIBRERIA PERO SE LES LLAMA MEJOR modules

script, uno, dos, tres, th = argv         #SE TIENEN QUE PONER 3 ARGUMENTOS QUE ES A LO QUE SELLAMA UNPACK
                                          #QUE ES UN CONJUNTO DE VARIABLES QUE SE DAAN EN EL CODIGO
print "The script is called:", uno        #EL TERMINO [ argv ] SIGNIFICA "ARGUMENT VARIABLE"
print "The first variable is:", script
print "The second variable is:", tres
print "The third variable is:", dos

#SOLO SE PUEDE IMPRIMER EN LA CONSOLA/CMD
#NO IMPORTA LOS NOMRBRES QUE SE LE PONGAN AL [ = argv ] SIEMPRE DARA COMO PROMER VALUE EL NOMBRE DEL script
#IMPRIME EN LOS LUGARES QUE SE LES MARCA EN EL print
#ASI ES COMO IMPRIME ESTE CODIGO.
#The script is called: 1
#The first variable is: Ex13.py
#The second variable is: 3
#The third variable is: 2
