# set1={1,5,7,5}
# print(set1)

# set2 ={}
# print(type(set2))


#pyhon program to demonstrate intersection of two set
set1=set()
set2=set()

for i in range(5):
    set1.add(i)
for i in range(3,9):
    set2.add(i)

        #intersection using
        #intersection()function

set3 = set1.intersection(set2)
print("intersection using intersection() function")
print(set3)

#intersection using "&" operator)
set3 = set1 & set2
print("\nintersection using '&' operator")
print(set3)