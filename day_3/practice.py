print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7//3
if floor_division == int(2.7):
    print("true")

#Check if type of '10' is equal to type of 10
str_10 = "10"
num_10 = 10
if type(str_10) == type(num_10):
    print("true")
else:
    print("false")

# Check if int('9.8') is equal to 10
if int(float("9.8")) == 10:
    print("true")
else:
    print("false")

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hour = int(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hour * rate_per_hour
print("Pay:", pay)

# # Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years: "))
seconds = years * 365 * 24 * 60 * 60
print("Number of seconds a person can live:", seconds)

for i in range(1,6):
    print(f"{i}, {i**0}, {i**2}, {i**3}")