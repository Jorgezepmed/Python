#PRINTING FORMAS, SALTOS DE RENGLON

formatter = "%r %r %r %r"                   #DECLARAS EL FORMATO QUE TENDRAS DE NUEMOERS O PALABRAS, FOLTANTES AL PARECER

 print formatter % (1, 2, 3, 4)
 print formatter % ( "one", "two", "three", "four")
 print formatter % (True, False, False, True)
 print formatter % (formatter, formatter, formatter, formatter)
 print formatter % (
 " I had this thing.",
 "That you could type up right.",
 "But it didn't sing.",
 "So i said goodnight"

 )

#PARA HACER SALTOS DE RENGLON SE LE AGREGA A LAS PALABRA [ "Jan\n"] ASI LA PALABRA SIGUENTE BRINCARA UN RENGLON
#SI ESCRIBES [ print """ PODRAS ESCIRBIR, SALTAR RENGLONES, ESPACIOS, ETC Y TE LO RESPERTARA HASTA QUE CIERRRES CON OTO """ ]
# COMO EJEMPLO A LO ANTEROIR
#  print """
#      Hola esto era hace una vez una ni;a
#      muy linda que se portaba bien, vivia en un castillo
#      ble bla bla bla,
#   """
