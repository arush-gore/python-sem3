a = int(input("Enter the value of a. "))
b = int(input("Enter the value of b. "))

print(f"& operator output {a} and {b} is",a&b)

print(f"Left shift output ({a} is shifted to the left by {b} places) is ",a<<b)
#This can also be calculated as a*(2^b)

print(f"Right shift output ({a} is shifted to the right by {b} places) is ",a>>b)
#This can also be calculated as a/(2^b)

print(f"Identity operator output of {a} and {b} is ",(a is b))
print(f"ID of {a} is ",id(a))
print(f"ID of {b} is ",id(b))


#Membership operator
str1 = str(input("Enter your string. "))
str2 = str(input("Enter the substring you want to find in the word."))
if ((str2 in str1) == True):
    print("Your string was found.")
else:
    print("Your string was not found.")

