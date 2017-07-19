#Variables y Printing

my_name = 'Jorge David Zepeda'   #CADA VEZ QUE SE USEA EL '' SE CREA UN STRING
my_adge = 21                    # UNA VARIABLE NO PUEDE EMPEZAR COMO NUMERO, TIENE QUE SER UN CARACTERN
my_height = 1.78    #METROS
my_weighy = 84      #KILOGRAM
my_eyes = "Brown"
my_haire = "Brown"

print "Let's talk about %s." % my_name            #ES LO MISMO SI EL "%" ESTA PEGADO O NO A LA VARIABLE
print "He is %d metros tall." %my_height
print "He's %d kilogram heavy " % my_weighy
print "He's got %s eyes and %s hair" % (my_eyes, my_haire)   #DEBE DE TENER LOS ( ) PARA QUE PUEDA CORRER


print "If i add %d, %r, and %r I get %r." % (my_adge, my_height, my_weighy, my_adge + my_height + my_weighy)

# %r SE USA PARA NUMEROS CON PUNTO DECIMAL
# %d PARA NUMEROS ENTEROS
# %s PARA PALABRAS/STRIN
