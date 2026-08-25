applications = []
for i in range(1,6):
    applications.append(str(input(f"Enter application no. {i}: ")))
print(f"Your final list of applications is: {applications}")

reply = int(input("Do you want to edit the list? Press 1 for Yes and 2 for No."))
if reply == 1:
    ind = int(input("Which application no. do you want to add?"))
    while (ind>6 or ind<1):
        ind = int(input("The application no. you have entered is invalid. Please re-enter."))
    edit = str(input("What application will you replace it with?"))
    applications.insert((ind-1),edit)
    print(f"Here is your edited list: {applications}")
elif reply == 2:
    print("Ok, no worries!")
else:
    print("Invalid.")