#LOOPS AND LISTS

the_count = [1, 2, 3, 4, 5]                                            # ESTA ES LA FORMA DE HACER LISTAS CON NUMEROS, QUE ES MASO COMO UNA MATRIZ
fruits = [ 'apples' , 'oranges', 'pears', 'apricots']                  # FORMA DE ESCIRBIR LISTAS CON STRING SIEMPRE ENTRE ' ' Y ,
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This first kind of for-loop goes through a list

for number in the_count:                                               #for LA VARIABLE QUE SE VA A ITERAR  in EN LA SECUENCIA TAL
    print "This is count %d" % number

#Same as above

for fruit in fruits:                                                   #NO IMPORTA EL NOMBRE QUE LE PONGAS A LA VARIABLE DESPUES DEL FOR 
    print "A fruit of type: %s" % fruit

#Also we can go through mixed lists too
#Notice we have to use %r since we don't know what's in it

for i in change:
    print "I got %r" % i

# We can also build lisits, first strat with an empty one
elements = [ ]

#Then use the range functions to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # Append is a functions\ taht lisits Understan
    elements.append(i)

#Now we can prin them out too
for i in elements:
    print "Element was: %d" % i



#EN EL FOR SE EJECUTA LAS VECECS QUE LA SECUENCIA DICTA HASTA QUE SE ACABE
