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
#Cut(slice) out the first word of Coding For All string.
print("Coding For All"[7:])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding For All".index("Coding"))
print("Coding For All".find("Coding"))
print("Coding For All".startswith("Coding"))
text = "Coding For All"
if("Coding" in text):
    print("Yes, 'Coding' is found in the string.")
print(text.count("Coding")>0)

#Replace the word coding in the string 'Coding For All' to Python.
print(text.replace("Coding","Python"))

#Split the string 'Coding For All' using space as the separator (split()) .
print(text.split())

text1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(text1.split(","))

# What is the character at index 0 in the string Coding For All.
print(text[0])
#What is the last index of the string Coding For All.
print(text[-1])
print(text[11])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase1 = "Python For Everyone"
print("".join([word[0] for word in phrase1.split()]))
#Create an acronym or an abbreviation for the name 'Coding For All'.
phrase2 = "Coding For All"
print("".join([word[0] for word in phrase2.split()]))

#Use index to determine the position of the first occurrence of C in Coding For All.
print(text.index("C"))
#Use index to determine the position of the first occurrence of F in Coding For All.
print(text.index("F"))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(text.rfind("l"))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence1 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence1.find("because"))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence1.rindex("because"))
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence1[sentence1.find("because"):sentence1.rindex("because")+len("because")])

#Does 'Coding For All' start with a substring Coding?
if(text.startswith("Coding")):
    print("yes")
else:
    print("no")    
#Does 'Coding For All' end with a substring coding?
if(text.endswith("coding")):
    print("yes")
else:
    print("no")

#' Coding For All      '  , remove the left and right trailing spaces in the given string.
new_text = "   Coding For All      "
print(new_text.strip())


""" Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython # false
thirty_days_of_python """  # true
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#".join(list))

#Use the new line escape sequence to separate the following sentences.
s = "I am enjoying this challenge.\nI just wonder what is next."
print(s)

radius = 10
area = 3.14 * radius **2
print(f"The area of a circle with radius {radius} is {area}")

#Make the following using string formatting methods:
"""8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144"""
a =8
b=6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")