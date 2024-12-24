first_name ="ram"
second_name ="shyam"

print(first_name+second_name) #concat

a="ram"
b = 9
print(a+str(b))
first_sentence = "  hello i am from mars  "

print(first_sentence .strip()) #to remove extra space

skill_shikshya ="skillshikshya@gmail.com"

splitted_data = skill_shikshya.split('@')#tukraune kam grxa
print(splitted_data)

about_nepal ="nepal is .....nepal...huhfbvhbfhjfhi  india....india"
corrected_data = about_nepal.replace('india','nepal')#replace grxa eauta le aarko lai replace tag le 
corrected_data = corrected_data.replace('.','the')#correct grxa 
print(corrected_data)

father_name = "some name"
print(father_name.upper())#sabai lai capital grxa
print(father_name.capitalize())#agadi ko matra
print(father_name.title())


#classwork , describe any 10 string manipulation function with example
#1.casefold casefold() method returns a copy of a string with all characters in lowercase.

#  mother_name ="Pratima RAI"
# print(mother_name.casefold())

#lower()Returns True if all characters in the string are lower case
string1 = "Python"
string2 = "python"

# Case-insensitive comparison using lower() method
if string1.lower() == string2.lower():
    print("The strings are case-insensitive equal.")
else:
    print("The strings are not equal.")

# #3.splitlinesSplits the string at line breaks and returns a list
# father_name = "some name"
# print(father_name.splitlines())

# # #SWAPCASE Swaps cases, lower case becomes upper case and vice versa
# father_name = "some name"
# print(father_name.swapcase())

# # #imp
# # #len le count grxa length
# # #replace

# name = ["hello world" ,"nepal"]
# oo = " ".join(name)  # Joins the words with a space
# print(oo)

# # encode Returns an encoded version of the string
# father_name = "some name"
# print(father_name.encode())

# father_name = "some name"
# print(father_name.encode())


 #tommorrow condition
 


