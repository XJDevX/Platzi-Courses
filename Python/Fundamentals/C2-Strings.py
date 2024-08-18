#<<---Strings in Python--->>#

#->> Printing
print("\nNormal String: Hello") #Normal Strings

text = "Python" #Text's variable
print(f"Variable's text: {text}\n") #Printing text from variables

#->> Exploring the String
print(f"First letter: {text[0]}") #First letter of the String
print(f"Last letter: {text[-1]}\n") #Last letter of the String

#->> Concatenate Strings
name = "Python"
last_name = "Language"
print(f"Concatenate: {name} {last_name}\n") # Joining 2 Strings in one Print

#->> String's options
print(f"Lenght: {len(text)}") #Show the lenght of the String
print(f"Count 'P': {text.count('P')}") #Count characters
print(f"Find 'O': {text.find('o')}") #Finds a character into the String
print(f"Index of 'T': {text.index('t')}\n") #Show the index of a letter

textLower = text.lower
print(f"Text lower: {text.lower()}") #Print text in lowercase
print(f"Text UPPER: {text.upper()}") #Print text in UPPERCASE
print(f"Text Capitalize: {text.capitalize()}") #Puts every first letter in UPPERCASE
print(f"Text Title: {text.title()}") #Puts only the first letter in UPPERCASE
print(f"Text Swapcase: {text.swapcase()}\n") #Swap the cases of the Letters

print(f"Delete spaces: {text.strip()}") #Delete all spaces of the Strings
print(f"Replace text: {text.replace('O', '0')}\n") #Replace letters of the Strings