#code to demonstrate tuple data type
shoppingList=[];
shoppingList=["Watch", "Laptop", "Shoes", "Pen", "Clothes"];
shoppingList.append("Football")
print(shoppingList[0], "is the forst item on the list")
print(shoppingList[-1]," is the last item on list")
print(shoppingList[0:6]," is the whole list items")
print(shoppingList[1:3])
shoppingList[3]="Notebook"
del(shoppingList[4])
print(shoppingList)
print(shoppingList.index("Laptop"),"is the index of item Laptop")
