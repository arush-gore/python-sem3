def odd_even(n):
    if n % 2 == 0:
        print(n," is even")
    else:
        print(n, " is odd")

num = int(input("Enter a number: "))
odd_even(num)