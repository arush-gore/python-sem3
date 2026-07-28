#Examples of Arithmetic Operator
a = int(input("Enter the value of a. "))
b = int(input("Enter the value of b. "))

#Addition of numbers
add = a + b
# Subtraction of numbers
sub = a - b
# Multiplication of number
mul = a * b
#Division(float) of number
div1 = a / b
#Division(floor) of number
div2 = a // b
#Modulus (remainder)
mod = a % b
#Exponent (power)
pwr = a ** b

print(f"The addition of {a} and {b} is ",add)
print(f"The subtraction of {a} from {b} is ",sub)
print(f"The multiplication of {a} and {b} is ",mul)
print(f"The division (float) of {a} by {b} is ",div1)
print(f"The division (floor) of {a} by {b} is ",div2)
print(f"The remainder when {a} is divided by {b} is ",mod)
print(f"{a} raised to the power {b} is ",pwr)