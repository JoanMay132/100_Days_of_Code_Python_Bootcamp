states_of_america=["Delaware","Pennsylvania","sdfs","fafa"] #The order is determined by the order of the list
print(states_of_america[1]) #Remember programmers start to count from zero
print(states_of_america[-1]) #we print the last one, -1 is the last item in the list because you can´t really have minus zero.
states_of_america[1]="pensilvaina" #we can overwrite variables inside the list
print(states_of_america)

#We can add items to the end of the list with .append

states_of_america.append("Mexico")
print(states_of_america)

states_of_america.extend(["olaer"]) 
# .extend() ->Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable
print(states_of_america)

'''Recuerda Joan checar Data Structures'''
#list.insert(i, x)
#Insert an item at a given position.

#list.remove(x)
#Remove the first item from the list whose values is equal to x. 

#list.pop([i])
#Remove the item at the given position in the list, and return it. If no index is specified, a.pop() 
#removes and returns the last item in the list.

#list.clear() -> Remove all items from the list. Equivalent to del a[:].

#list.count(x) -> Return the number of items x appears in the list.

#list.sort(key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization) 

#list.reverse()
#Reverse the elements of the list in place.

#list.copy()
#Return a shallow copy of the list. Equivalent to a[:]