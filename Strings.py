# What are strings?
# Anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. String are used when working with Unicode characters.
First_friend="Dhrubo"
Second_friend='Avee'

print("Hello, "+First_friend +" "+ Second_friend)
apple='He said, "I want to eat an apple"'
print(apple)

chat= '''hello, Arnab 
How are you?
I am fine
Where are you going today'''
print(chat)

Name="Arnab"
print(Name[0])
print(Name[1])
print(Name[2])
print(Name[3])
print(Name[4])

print("printing character using for loop\n")
for character in chat:
    print(character)
