#<<---How to use Loops in Python--->>#
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers: #Analize all the elements into a List
    print(f"I is equals to: {i}")
print("\n")

for i in range(10): #Use the same numbers but instead of a List
    print(f"Range(I) is equals to: {i}")
print("\n")

fruits = ["Apple", "Pineapple", "Orange", "Strawberry", "Tomato"]
for fruit in fruits: 
    print(f"Analized value: {fruit}")
    if fruit == "Orange":
        print(f"\nIn the set is an Orange!\n")
print("\n")

x = 0
while x <= 10: #An Statement Loop that will be executed until something happends
    print(f"The x's value is: {x}")
    x += 1
print("\n")