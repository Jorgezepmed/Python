#READING FILES


from sys import argv

script, filename = argv

txt = open(filename)                            #CREAMOS LA COANSTANTE txt Y LE DAMOS LA INSTRUCCION DE QUE ES IGUAL A open(nombre)
                                                #PUEDE TENER CUALQUIER NOMBRE, EL filename SE DA POR EL argv

print "Here's  your file %r:" % filename
print txt.read()                                #AQUI ES DONDE ABRE EL ARCHIV QUE LLAMAMOS txt CON EL .read()


print "Type the filename again:"
file_again = raw_input(">>")                    #LE DAMOS OTRO NOMBRE DE VARIABLE AL PROGRAMA  PERO ES EL MISMO ARCHIVO DE TEXTO

txt_again = open(file_again)

print txt_again.read()
