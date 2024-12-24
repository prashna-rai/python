class Calculator:
    def sum(self ,a,b): 
        print("addition of two number is :",a+b)
    def multiply(self ,a,b):
        
        print("multiplication of two number is :",a*b)
   
    def sub(self ,a,b):
        
        print("subtraction of two number is :",a-b)
c1=Calculator()
c1.sum(5,10)
c1.multiply(7,4)
c1.sub(90,90)

class Calculator:
    def __init__(self, first_number,operator,second_number):
        print("this is initializing...")
        self.first_number= first_number
        self.second_number= second_number
        self.operator= operator
        
    def result(Self):
        if Self.operator == "+":
             return Self.add()
        elif Self.operator == "*":
           return Self.multiply()
        
    def add(self):
        return self.first_number + self.second_number
    
    def multiply(self):
        return self.first_number * self.second_number
    
cal_obj = Calculator(4,"*",8)
output = cal_obj.result()
print("calculation of two number is ",output)

