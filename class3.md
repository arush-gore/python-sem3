# String Concate

```python
str1 = "python"
str2 = "programming"
str3 = str1 + str2
print(str3)
# to print a space between two strings with the help of double quotations
str3 = str1 + " " + str2
print(str3)

# to print length of a string
print(len(str1))
s4 = len(str3)
print(s4)
```
# String Indexing, Slicing and Negative Indexing

```python
# indexing [] means to get the location of each character. It starts from 0th location.
str5 = "pune"
ch = str5[1] #it displays 1's place of string
print(ch)

# slicing is used in machine learning for data analysis
str = "I like to study"
print(str[2:6])
print(str[2:len(str)]) # here len(str) shows at the end of string means it has started from 2nd location to end of string
#another way
print(str[2:])
print(str[:4])

# negative index means to calculate index backward counting
str7 = "apple" # here e=-1, l=-2. p=-3, p=-4, a=-5
print(str7[-3:-1])
```
It is used as str[<start>:<end>:<increment/decrement>]

# Operators
They act on operands  

## Types of operators:
- Arithmeitc
- Relational
- Logical
- Bitwise
- Assignment
- Identify
- Membership

## Arithmetic Operators
| Operator | Name | Example |
| --- | --- | --- |
| + | Addition | x+y |
| - | Subtraction | x-y |
| * | Multiplication | x*y |
| / | Division | x/y |
| % | Modulus | x%y |
| ** | Exponentiation | x**y |
| // | Floor Division | x//y |
| +=, -=, *=, /= | Augmented Assignment | x+=y |
