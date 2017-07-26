#WHILE LOOPS

i = 0
numbers = [ ]

while i < 6:
    print "At the top i is %d" %i
    numbers.append(i)

    i = i + 1

    print "Numbers now:", numbers
    print "At the botton i is %d" %i


print "The numbers:"

for num in numbers:                     #SE IMPIMER UNA LISAT CIN TODOS LOS NUMEROS QUE HAY EN numbers
    print num

#EL WHILE FUNCIONA SIEMPREY CUANDO SEA TRUE LA FUNCION
#FUNCIONA DE UNA MANERA EN LA TENEMOS COMO PRINCIPO i = 0, Y QUEREMOS EL while DE I A 6
#ENTONCES IMPIMIMOSVALOR DE i, AGREGAMOS QUE CUANDO LLAMEMOS A LA VARIALE numbers (QUE NO TENEMOS AUN VALORES DECLARADOS)
# SE IMPRIMIRA AL FINAL LA ULRIMA VARIABLE i conociada
#DESPUES SE LE SUMA 1 A i E IMPIMIMOS numbers Y SE IMPRIMEN LAS iS QUE YA PASARON Y LA UTLIMA i
