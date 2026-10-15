my_list= [1, 2, 3, 4, 5, 6, 11, 3, 33]
number = 3
index = 0
for a in my_list:
    if (a == number):
        print(f"{number} was found at index {index}")
        break
    index+=1