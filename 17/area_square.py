def calculate_area(side):
    return side ** 2
side = float(input("Enter the side length of the square. "))
area = calculate_area(side)
print(f"The area of the square is :{area} ")