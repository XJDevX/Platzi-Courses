#<<---List in Python--->>#
thingsToDo = [ #Basic structure of lists
    "Hospedate in the hotel",
    "Lunch pizza or burgers",
    "Visit the city's museum",
    "Drink an excellent coffe in Starbucks"
]

#->> Access to certain positions of Lists
firstThing = thingsToDo[0] #Enter the first position
print(f"The first thing to do is: {firstThing}")
lastThing = thingsToDo[-1] #Enter the last position
print(f"The last thing to do is: {lastThing}")

#->> Special options
print(f"Things to do until third: {thingsToDo[0:2]}")
print(f"Things to do from second one: {thingsToDo[1:]}")

#-> Modify the lists
thingsToDo.append("Sleep in a soft bed") #Add an item in the last position
thingsToDo.insert(1, "Walk in the city's park") #Add an item in a certain position
del thingsToDo[-1] #Delete a certain item

#-> Slicing with lists
myList = [1, 2, 3, 4, 5]
copyOfList = myList[:] #Right way to copy a List without having toubles of mirroring