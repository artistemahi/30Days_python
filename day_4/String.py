# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
s1 = "Thirty"
s2 = "Days"
s3 = "Of"
s4 = "Python"
result = s1 + " " + s2 + " " + s3 + " " + s4
print(result)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
s1 = "Coding"
s2 = "For"
s3 = "All"
sentence = f"{s1} {s2} {s3}"
# print(sentence)

#Declare a variable named company and assign it to an initial value "Coding For All".
company = sentence

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())