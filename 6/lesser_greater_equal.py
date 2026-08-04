num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = f"{num1} is greater than {num2}." if num1>num2 else f"{num1} is lesser than {num2}." if num1<num2 else f"{num1} is equal to {num2}."
print(result)