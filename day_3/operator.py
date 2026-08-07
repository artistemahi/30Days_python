from math import sqrt 
age = 21
height = 180
complex = 1+2j

# finding the area of the triangle
base = float(input("enter the base : "))
height = float(input("enter the height :"))
area = (base*height)/2
print("Area of triangle is : ",area)

# finding the perimeter of the triangle 
a,b,c = float(input("enter the first side of triangle :")),float(input("enter the second side of triangle :")),float(input("enter the third side of triangle :"))
perimeter = a+b+c
print("perimeter of triangle is :",perimeter)

# finding the area and perimeter of rectangle
length , width = float(input("enter the length of rectangle :")), float(input("enter the width of rectangle :"))
area = length*width
perimeter = 2*(length+width)
print("area :",area," perimeter :",perimeter)

""" Get radius of a circle using prompt.
 Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
"""
radius = float(input("enter the radius of the circle :"))
pi =3.14
area = pi*radius*radius
circumference = 2*pi*radius
print("area of circle is : ", area, "circumference of circle is :",circumference)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope1 = 2
x_intercept = 2/2
y_intercept = -2
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope2 = (10-2)/(6-2)
distance = sqrt((6-2)**2 + (10-2)**2)
if slope1 == slope2:
    print("slope1 and slope2 are equal")
elif slope1>slope2:
    print("slope1 is greater than slope2")
else:
    print("slope2 is greater than slope1")

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x_value = -3
y_value = x_value**2 + 6*x_value + 9
if y_value ==0:
    print(f"y is {y_value} when x is {x_value}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
if len("python") != len("dragon"):
    print("length of python and dragon are not equal")

if "on" in "python" and "on" in "dragon":
    print("true")

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
if "jargon" in sentence:
    print("true")
else:
    print("false")

statement = "on" not in "python" and "dragon"
print("There is no 'on' in both dragon and python:", statement)

length_of_python = float(len("python"))
string_number = str(length_of_python)
