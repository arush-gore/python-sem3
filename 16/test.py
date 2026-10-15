num = int(input("How many elements do you want to add in the list"))
mylist = []
for i in range(num):
    item = int(input(f"Enter element:"))
    mylist.append(item)
print("Your final list is:", mylist)