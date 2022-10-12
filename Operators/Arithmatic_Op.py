"""
Menu driven calculator and use of functions
"""

def add(a,b):
   ans = a + b
   return ans

def sub(a,b):
   ans = a - b
   return ans

def mul(a,b):
   ans = a * b
   return ans

def div(a,b):
   rem = a % b
   quo = a / b
   print("Remainder is",rem,"and Quotient is",quo)


print(" Welcome to the calculator  ")

a = int(input("Enter variable 1 :"))
b = int(input("Enter variable 2 :"))

print(" Which operation do you want to carry out?")
opp= int(input("Enter \n  1 for addition  \n 2 for subtration \n 3 for multipication \n  4 for division \n ---> :"))
               
if opp == 1:
    print(add(a,b))
       
elif opp == 2:
    print(sub(a,b))
         
elif opp == 3:
    print(mul(a,b))  
         
elif opp == 4:
    print(div(a,b))         
         
  
