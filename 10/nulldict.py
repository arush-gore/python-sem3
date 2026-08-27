null_dict = {}
null_dict["Name"] = "Arush"
print(null_dict)

#Nested Dictionary
student = {"Name":"Arush",
           "City":"Pune",
           "Taluka":"Haveli",
           "Subject":{
               "Python":80,
               "Java":79,
               "C_Program":78
            }
           }
print(student)
print(student["Subject"])
print(student["Subject"]["Python"])
print(student.keys())
print(len(student))
print(student.values())
print(list(student.values()))
print(student.items())
print(list(student.items()))

'''
print("Welcome to the dictionary creation UI.")
len = int(input("How many entries do you want?"))
dict = {}
for i in range(len):
    choice = int(input("Press 1 to continue. Press 2 to make nested dictionary."))
    if choice == 2
'''