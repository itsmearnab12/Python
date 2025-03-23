# Note: String are immutable means it not change the existing string but will create a new string.
# The len function is used to find the length of the string.
a="Arnab"
print(len(a))

# The upper() method converts a string to upper case.
print(a.upper())

# The lower() method converts a string to lower case.
print(a.lower())

# The rstrip() removes any trailling characters.
# note The rstrip() method removes the trailling characters. it will not remove the leading characters 
b="!!Arnab!! &&Keyur&& **Aman**"
print(b.rstrip("!"))

# The replace() method replace all occurance of a string with another string.
print(b.replace("Arnab", "Dhrubo"))

# The split() method splits the given string at the specified instance and return the separated string as list items.
print(b.split(" "))

# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
Heading="introduction to python"
print(Heading.capitalize())

# The center() method aligns the string to the center as per the parameters given by the users 
str1="Welcome to video of string methods"
print(str1.center(50))

# The count() method returns the number of times the given value has occured within the given string.
str1="!!Arnab!! **Aman** &&Avee&& !!Aman!!"
print(str1.count("Aman"))

# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str2="Arnab!!!"
print(str2.endswith("!!!"))

# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string the return -1.
str2="He's name is Arnab. He is an honest man."
print(str2.find("is"))

# The index() method searches for the first occurrence of the given value and return the index where it is present. If given value is absent from the string then rasise an exception.
print(str2.index("Arnab"))

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns false.
str2="Welcometoconsole09"
print(str2.isalnum())

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or number(0-9) are present, then it returns False 
print(str2.isalpha()) 

# The islower() methods returns True if all the characters in the string are lower case, else it returns False.
str3="HELLO TO EVERYONE"
print(str3.islower())

# The isprinyable() method returns True if all the values within the given string are printable, if not, then return False.
print(str3.isprintable())

# The isspace() method returns True only and only if the string contains white spaces, else returns False.
str4="     "
print(str4.isspace())

# The istitle() returns True only if the first letter of each word of the string is capitalized, else it returns False
str5="Hello Every One"
print(str5.istitle())

# The isupper() methods returns True if all the characters in the string are upper case, else it returns False.
str3="HELLO TO EVERYONE"
print(str3.isupper())

# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
print(str5.swapcase())

# The title() method capatilized each letter of the word within the string.
str6="his name is arnab"
print(str6.title())