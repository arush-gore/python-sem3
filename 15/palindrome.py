num = int(input("Enter your number."))

temp = num
rev = 0

while temp>0:
    rev = rev*10 + temp%10
    temp//=10

if num == rev:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")