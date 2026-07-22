# indexing [] means to get the location of each character. It starts from 0th location.
str5 = "pune"
ch = str5[1] #it displays 1's place of string
print(ch)

# slicing is used in machine learning for data analysis
str = "I like to study"
print(str[-1:6])
print(str[2:len(str)]) # here len(str) shows at the end of string means it has started from 2nd location to end of string
#another way
print(str[2:])
print(str[:4])

# negative index means to calculate index backward counting
str7 = "apple" # here e=-1, l=-2. p=-3, p=-4, a=-5
print(str7[-3:-1])