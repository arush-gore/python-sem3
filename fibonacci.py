# Print Fibonacci series using while()

n = int(input("Enter how many terms as a input: "))
n1, n2 = 0, 1
#print initial two numbers
print(n1, n2, end=' ')

i=0
while(i<n-2): #here we know first initial number
    n3 = n1 + n2
    print(n3, end=' ')
    n1 = n2
    n2 = n3
    i = i + 1
