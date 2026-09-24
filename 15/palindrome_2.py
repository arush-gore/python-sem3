i = int(input("How many numbers do you want in your list? "))

numlist = []

for x in range(i):
    tempnum = int(input(f"Enter your number {x+1} "))
    numlist.append(tempnum)

print(numlist)

palindrome = []

for num in numlist:
    temp = num
    rev = 0
    while temp>0:
        rev = rev*10 + temp%10
        temp//=10
    if num == rev:
        palindrome.append(num)

print(f"Your list of palindromes is {palindrome}.")