countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)      #Converting tuple to list 
temp.append("Russia")       #Add item
temp.pop(3)                 #Delete item
temp[2] = "Finland"         #Change item
countries = tuple(temp)     #Converting list to tuple 
print(countries)

tuple1= (0, 1, 2, 31, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
res = tuple1.index(3, 4, 8)
print(res)