#ASKING QUESTIONS

print "How old are you?",                 #LAS COMAS HACEN QUE LA RESPUESTA SE ESCRIBA EN SEGUIDA DE LA PREGUNTA
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %s old, %r tall and %r heavy." % (age, height, weight)   #POR SER [%r] NOS LO VA A IMPRIMIR CON '' EL RESULTADO ENTRE EL TEXTO

#SI FUERA UN [%s] DE STRING SI LO IMPRIMIRIA SIN LOS '' 
