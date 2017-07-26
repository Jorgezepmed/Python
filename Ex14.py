#PROMPTING AND PASSING

from sys import argv                        #LLAMAMAOS A LA MISMA LIBRERIA QUE EL PASADO Ex13

script, user_name = argv
prompt = '>'                                  # SE ESTA IGUALANDO EL prompt A UNA VARIABLE QUE ES LA QUE APARECERA EN LA TERMINAL Y ENSEGUIDA SE ESCIBIRA LA RESPUESTA
                                              # [prompt] CONJUNTO DE CARATERES QUE ESPERAN UNA ORDEN,
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions"
print "Do you like me %s?" % user_name
likes = raw_input(prompt)                       #SE ESTA EN PARENTECIS DEPUES DE raw_input PORQUE ESTA LLAMDADO UN %s QUE SERA IMPRESA

print "Where do you live %s? " % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about likingme.
You live in %r. Not sure shere that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

#LINEA 6 EL [prompt] PUEDE SER LLAMADA COMO SEA.
