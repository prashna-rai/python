# def display(n):
#     print(n)
#     if n<9:
#         display(n+1)
# display(0)        

#wap to print square number using recursion function from 1 to 50

# def square_number(n):
#     print(n**2)
#     if n<50:
#         square_number(n + 1)
# square_number(0)

# wap to make fibonacci series upto n term

# a=0
# b=1
# print(a)
# print(b)
# for i in range (10):
#     c=a+b
#     print(c)
#     a=b
#     b=c   
# assignmnet by using recursion function

def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    print(a)
    fibonacci(n-1, b, a+b)


num = 10
fibonacci(num)



   