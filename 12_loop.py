# loop types
# while Loop 
# for loop 

# while True:
#     print("HELLO NPL!!!")

# i = 0
# while(i<100):
#     print("hello")
#     i=i+1

    #WAP TO FIND THE NUMBER IS ODD OR EVEN
# num = 1
# while(num<=50):
#     if (num%2 == 0):
#         print(num, "is even")
#     else:
#         print(num ,"is odd")
#     num = num+1
    

#wap to check 5 is prime number or not?
num = 11
count = 0
start = 1

while start<=num:
    if num%start ==0:
        count=count+1
        start=start+1

        if count <=2:
            print(f"{num} is prime number")
        else:
            print(f"composite number {num}")
