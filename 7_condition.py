#types of condition 
# if
# else
# elseif elif(nested condition)    
# age=13
# if age>18:
#     print("you can vote")
# else:
#     print("you cannot vote")

# syntax
#     if condition true :
# statements

# age = 18
# if age<20:
#     print("you can marriage")

#WAP to output like {child,adult...old}

# if age > 0:
#     print("you are child")
#     if age > 12:
#         print("you are teenager")
#         if age < 20:
#             print("you are adult")
#             if age < 60:
#                 print("you are old")

# classwork
# age = "A"

# if age.isdigit() == False:
#  print("invalid age")

# elif age>0 and age<13:
#  print("you are child")

# elif age>=13 and age<20:
#  print("you are teenagers")

# elif age<0 or age>200:
#  print("wrong input")

# else:
 
#  print("either you are adult or old")

age = 87
if isinstance(age,str) and age.isdigit() == False:
    print("invalid age")

elif age>0 and age<13:
    print("you are child")

elif age>=13 and age<20:
    print("you are teenagers")

elif age<0 or age>200:
    print("wrong input")

else:
    print("either you are adult or old")

 
