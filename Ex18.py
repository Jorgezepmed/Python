#NAMES, VARIABLES, CODE, FUNCTIONS

#This one is is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r " % (arg1, arg2)



#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):                                    #
    print "arg1: %r, arg2: %r " % (arg1, arg2)

#This just take one argument
def print_one(arg1):
    print "arg1: %r " %arg1

#This one takes no arguments
def print_none():
    print "I got nothing'."

print_two("Jorge", "Zepeda")
print_two_again("Jorge", "Zepeda")
print_one("First!")
print_none()
