#Selection in Python is made using the two keywords 'if' and 'elif' and else (elseif)

#Python program to illustrate selection statement

mark = int(input("Enter your marks! "))
if mark >= 80:
    print("Grade is A.")
elif mark >= 65:
    print("Grade is B.")
else:
    if mark >= 50:
        print("Grade is C.")
    else:
        print("Grade is D.")
