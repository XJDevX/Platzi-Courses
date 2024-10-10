#<<---Dicts--->>#
myDict = {
    "Python": "Developer's paradise",
    "Platzi": "A nice platform to learn Technology",
    "Freddy Vega": "The CEO of Platzi",
    "Example": "Example Value"
}

#-->> Modify Dicts
print(f"Original: {myDict}\n")
del myDict["Example"] #Delete Values and Keys of the Dict
keys = myDict.keys() #Keys
values = myDict.values() #Values
items = myDict.items() #Items of the Dict
