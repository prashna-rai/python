my_tuple=(1,2,3,4)
print(my_tuple[0])

#unpacking
my_tuple=(10,20,30)
a,b,c = my_tuple
print(a,b,c)

person_info =("john", 30 ,"engineer")
name , age , profession = person_info
print(f"Name:{name}")
print(f"Age:{age}")
print(f"profession: {profession}")

my_tuple=(1,2,3,4)
print(my_tuple.count(2))
# by usibg index
print(my_tuple.index(3))


detail=("prashna" , 40 , "student")
name , age , profession = detail
print(detail)
