# Note as a and b are string so the output will be 12 not 3
a="1"
b="2"
print(a+b)

# Note as the a and b are integer so here the output will be 4 
a1=1
b1=3
print(a1+b1)

# Typecasting 
# As here both a and b are string and when we add them output is 12 but using typecasting concept we can convert string into integer
a="1"
b="2"
print(int(a)+ int(b))
# Now the after this the output will be 3 not 12

String = "15"
number = 7
string_number = int(String)
num = number + string_number
print("The sum of both the number is:",num)