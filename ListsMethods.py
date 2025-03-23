l = [9, 6, 8, 1, 2, 3, 4, 5, 1]
print(l)
l.append(7) #This will add the element at the end of the list
print(l)

l.sort() #This method sorts the list in ascending order. The original list is updated
print(l)

l.reverse() #This method reverse the order of the list.
print(l)

print(l.index(1)) #This method returns the index of the forst occurance of the list item.
print(l)

print(l.count(1)) #This returns the count of the number of items with the given value.
print(l)

l.insert(1, 999) # This  method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
print(l)

m = [9 , 99, 998]
l.extend(m) #This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
print(l)


