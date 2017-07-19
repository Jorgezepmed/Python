#STRINGS AND TEXT


x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % ( binary, do_not)


print x
print y

print "I said: %r. " % x       #LA %r ES PARA debugging
print "I also said %r. " % y   # SE IMPRIME   [ I said: 'There are 10 types of people.']
                               # Y EL OTRO [ I also said "Those who know binary and those who don't"]
                               # EL PRIMERO SE IMPRIME CON '' Y EL SEGUNDO CON ""


hailarius = False
joke_evaluation = "Isn't that joke so funny?! %r"   #AL PARECER AGARRA EL ULTIMO VALOR, NO CONFIRMADP

print joke_evaluation % hailarius

w = "This is the left side of..."
e = "A string whit a right side."

print w + e
