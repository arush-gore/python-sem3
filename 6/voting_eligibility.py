age = int(input("Enter you age. "))
result = "Congratulation! You are eligible to vote." if age>=18 else f"Sorry, you are not eligible to vote. Please wait {18-age} more years!"
print(result)
