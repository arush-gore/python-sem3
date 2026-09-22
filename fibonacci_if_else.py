# Print Fibonacci series with while() and if else

n = int(input("Enter how many terms as input: "))

n1, n2 = 0, 1
i = 0

#check if number of terms is valid
if n<=0:
    print("Enter a positive integer.")

elif n == 1:
    print("Fibonacci series for ", n, "term:")
    print(n1)

else:
    print("Fibonacci series for ", n, "terms:")
    while i < n:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        i+=1
