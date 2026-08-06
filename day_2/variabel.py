# starting day 2

# declaring the  variables
first_name = "mahesh"
last_name = "kumar"
full_name = first_name + " " + last_name
country = "india"
city = "uk"
age = 21
year = 2004
is_married = False
is_true = True
is_light_on = False

# multiple variable assignment
is_handsome, is_good, is_perfect, is_ugly = True, True, True, False

# checking the data types of the variables
print(type(first_name),type(last_name),type(full_name),type(country),type(city),type(age),type(year),type(is_married),type(is_true),type(is_light_on))
# checking the  length of the variables
print(len(first_name),len(last_name),len(full_name),len(country),len(city),len(str(age)),len(str(year)),len(str(is_married)),len(str(is_true)),len(str(is_light_on)))

length_of_first_name = len(first_name)
length_of_last_name = len(last_name)

# comparing the variables
if(length_of_first_name > length_of_last_name):
    print("your first name is longer than your last name")
else:
    print("your last name is longer than your first name")    

# declaring the variables
num_one = 5
num_two =4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# radius of circle = 30m 1.area , 2.circumference
radius = 30
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2*3.14*radius

# take radius from user and calculate the area 
radius = input("enter the radius of the circle: ")
area_of_circle = 3.14 * (int(radius) ** 2)  # input function returns a string, so we need to convert it to float or int before calculation

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("enter your first name: ")
last_name = input("enter you last name: ")
country = input("enter your country: ")

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help("keywords")