def CalculateGmean(a, b):
    mean = (a*b)/(a+b)
    print("Harmonic Mean of both the number is:",mean)

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
if(a>b):
    print("First Number is greater")
elif(b>a):
    print("Second Number is greater")
else:
    print("Both The Number are equal")
CalculateGmean(a, b)

def islesser(c, d):
     pass
#By writing pass inside a function it will not through an error if we want to write the code in future

# c = 16
# d = 8
# CalculateGmean(c, d)