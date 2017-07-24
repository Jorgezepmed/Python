#FUNCTIONS AND VARIABLES
def cheese_and_crackers(cheese_count, boxes_of_crackers):                       #DEFINE LA FUNCION QUE CONSTA DE DOS VARIABLES
    print "You have %d cheeses! " % cheese_count                                #LA FUNCON CONSTA DE LAS 4 LINES DE print
    print "You have %d boxes of crackers! " % boxes_of_crackers
    print "Man that's enough fot a party! "
    print "Get a blanket.\n"


print "We can just give the function numbers directly"                          #SE DECLARAN LAS VARIABLES SABIENDO CUAL FUE DECLARADA PRIERO EN EL def
cheese_and_crackers(20, 30)

print "Or, we can use varibles from our script"
amount_of_cheese = 10                                                           #SE DECLARAN LAS VARABLES POR SEPARADO
amount_of_crackers = 50
cheese_and_crackers (amount_of_cheese, amount_of_crackers)                      #SE DECLARA LAS VARIABLES JUSTO COMO EN EL PRIMERO


print "We can even do math inside too:"
cheese_and_crackers(10 +20, 5 + 6)

print "And we can combine the two, varibles and math:"
cheese_and_crackers (amount_of_cheese + 100, amount_of_crackers + 1000)
