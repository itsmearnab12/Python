# Fout types of arguments in function

# Required arguments
def average(a, b):
    print("The Average is:", (a+b)/2)
average(4, 5)

# Default argument
def average(a=5, b=7):
    print("The Average is:", (a+b)/2)
average()
def average(a,b=7):
    print("The Average is:", (a+b)/2)
average(a=7)
# same for a as well

# Keyword argument
# we can provide argument with key = value, this  way the interpreter recognize the arguments by the parameter name. Hence, the order in which the argument are passed does not matter.
def name(Fname, Mname, Lname):
    print("Hello", Fname, Mname, Lname)

name(Lname="Lalu", Fname="Avee", Mname="Parsad")

# Variable length argument
