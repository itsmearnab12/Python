# Conditional Oprators >(Greater than), <(Smaller than), >=(Greater than equal), <=(Smaller than equal to), ==(Equal to), !=(Not equal to)
# if-statement
a = int(input("Enter Your Age: "))
print("Your Age is: ", a)
if(a>18):
    print("Your can dive")

print("\n")

# if-else statement
appleprize=200
budget=int(input("Enter Your Budget: "))
if(appleprize <= budget):
    print("Add 1KG apple to the cart")
else:
    print("Don't add apple to the cart")

print("\n")

# elseif statement
appleprize=100
budget= int(input("Enter Your Budget: "))
if(budget - appleprize >=400):
    print("Add 1KG apple to the cart")
elif(budget - appleprize >=300):
    print("You can still buy apples")
else:
    print("Don't add apple to the cart")

# Nested if statement
num = 18
if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<=10):
        print("Number is between 1 to 10")
    elif(num > 10 and num <= 20):
        print("Number is between 11 to 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")