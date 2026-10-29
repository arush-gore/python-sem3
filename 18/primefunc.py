def is_prime(number):
    # Numbers less than 2 are not prime
    if number < 2:
        return False
    # Check divisibilty  from 2 to number-1
    for i in range(2, number):
        if number%i == 0:
            return False
    return True

# Input from user
num = int(input("Enter a number: "))

# Check if the number is prime and print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")