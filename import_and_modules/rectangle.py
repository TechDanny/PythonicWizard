"""
Create a Python Program that calculates both the
perimeter and area of a rectangle
"""


from func_rectangle import Rectangle, Rectangle_area


length = int(input("Length: "))
width = int(input("Width: "))
perim = Rectangle(length, width)
area = Rectangle_area(length, width)
print(f"Perimeter of rectangle is: {perim}")
print(f"Area of rectangle is: {area}")
